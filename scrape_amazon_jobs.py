from playwright.sync_api import sync_playwright
import time
lis=[
    # 'https://jobs.smartrecruiters.com/Visa/744000046057885-sw-engineer-?source=LinkedIn',
    #  'https://www.amazon.jobs/content/en/career-programs/university/jobs-for-grads?category%5B%5D=Software+Development&country%5B%5D=IN#search'
    'https://in.indeed.com/jobs?q=software+engineer&l=&sc=0kf%3Aattr%286ETQT%7CDEM3E%7CEVPJU%7CGJUK3%7CX62BT%7CYEVMY%252COR%29attr%28CF3CP%29attr%28HFDVW%29%3B&from=searchOnDesktopSerp&vjk=b1ad3bd71a5cf598'
    ]
i=1

from bs4 import BeautifulSoup
def scrape_amazon_jobs(link):
    global i
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(link)     
        time.sleep(20)   
        # Wait for the content to load
        # page.wait_for_selector('div.job-tile')  # Adjust the selector as needed

        # Save the page content to a file
        bs = BeautifulSoup(page.content(), 'html.parser')
        for script in bs(["script", "style"]):
            script.decompose()
        text = bs.get_text()
        print(text)
       
      

# Extract job titles
# job_titles = page.query_selector_all('div.job-tile h3')  # Adjust the selector as needed
# for job in job_titles:
#     print(job.inner_text())

        browser.close()

if __name__ == "__main__":
    for link in lis:
        scrape_amazon_jobs(link)
    #     scrape_amazon_jobs()

