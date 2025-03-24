import os
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the AI_Engiene folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../AI_Engiene')))

from gemini_connect import Gemini_Connect

class JobScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def fetch_job_listings(self, job_title):
        self.driver.get(self.base_url)
        time.sleep(5)  # Wait for the page to load

        # Use Gemini to analyze the page and identify elements to interact with
        gemini = Gemini_Connect(agent_name="JobFinder")
        instructions = f"""
        Identify the search input field and the search button on the page. 
        Then, fill in the search input with '{job_title}' and click the search button.
        The response should be in the following JSON format:
        action
        [
            {
                "type": "input",
                "xpath": "XPATH_OF_SEARCH_INPUT",
                "value": "SEARCH_VALUE"
            },
            {
                "type": "click",
                "xpath": "XPATH_OF_SEARCH_BUTTON"
            }
        ]
        """
        page_content = self.driver.page_source
        print(page_content)
        with open("page_content.html", "w", encoding="utf-8") as file:
            file.write(page_content)
        actions_response = gemini.query(instructions + " " + page_content)
        actions_response = actions_response.strip("```json").strip("```")
        dict_of_actions = json.loads(actions_response)
        print(dict_of_actions)

        # Execute actions based on Gemini's analysis
        for action in dict_of_actions['actions']:
            if action['type'] == 'input':
                element = self.driver.find_element(By.XPATH, action['xpath'])
                element.send_keys(action['value'])
            elif action['type'] == 'click':
                element = self.driver.find_element(By.XPATH, action['xpath'])
                element.click()
            time.sleep(2)  # Wait for the action to complete

        # Re-analyze the page to find job links
        page_content = self.driver.page_source
        instructions = """
        Identify all the job postings in the current page and give in proper format of only plain text with a proper readable structure while giving links give in full format of baseurl. 
        I don't want any other information. I only need the job description and the URL all in compiled JSON format.
        The response should be in the following JSON format:
        [
            {
                "link": "FULL_URL_OF_JOB_POSTING",
                "description": "JOB_DESCRIPTION_TEXT"
            },
            ...
        ]
        """
        job_data_response = gemini.query(instructions + " " + page_content)
        job_data_response = job_data_response.strip("```json").strip("```")
        job_data = json.loads(job_data_response)
        print(job_data)

        job_descriptions = []
        for job in job_data:
            self.driver.get(job['link'])
            time.sleep(5)  # Wait for the job description to load
            job_description = self.driver.find_element(By.CSS_SELECTOR, 'div.job-description').text  # Adjust the selector as needed
            job_descriptions.append({
                'link': job['link'],
                'description': job_description
            })
            print(job_description)

        self.driver.quit()
        return job_descriptions

class JobAgent:
    def __init__(self, agent_name):
        self.agent = Gemini_Connect(agent_name=agent_name)

    def find_jobs(self, career_pages, job_title, instructions):
        all_jobs = []
        for page in career_pages:
            scraper = JobScraper(page)
            job_listings = scraper.fetch_job_listings(job_title)
            for job in job_listings:
                jobs = self.agent.query(f"{instructions} {job['description']}")
                all_jobs.append({
                    'link': job['link'],
                    'description': jobs
                })
        return all_jobs

if __name__ == "__main__":
    career_pages = [
        "https://www.amazon.jobs/content/en/career-programs/university/jobs-for-grads?category%5B%5D=Software+Development&country%5B%5D=IN",
        "https://www.hashicorp.com/en/careers/open-positions?workplaceType=Remote%2COnsite&department=Early%20Career%20Program%2CResearch%20%26%20Development"
    ]
    job_title = "Software Engineer"
    instructions = """
    Identify all the job postings in the current page and give in proper format of only plain text with a proper readable structure while giving links give in full format of baseurl. 
    I don't want any other information. I only need the job description and the URL all in compiled JSON format.
    The response should be in the following JSON format:
    [
        {
            "link": "FULL_URL_OF_JOB_POSTING",
            "description": "JOB_DESCRIPTION_TEXT"
        },
        ...
    ]
    """
    
    job_agent = JobAgent(agent_name="JobFinder")
    jobs = job_agent.find_jobs(career_pages, job_title, instructions)
    
    for job in jobs:
        print(job)