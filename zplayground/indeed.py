import requests
from bs4 import BeautifulSoup

def scrape_indeed_jobs():
    url = "https://www.indeed.com/jobs?q=software+engineer&l=remote"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    for job in soup.find_all("div", class_="job_seen_beacon"):
        title = job.find("h2").text.strip()
        company = job.find("span", class_="companyName").text.strip()
        link = "https://www.indeed.com" + job.find("a")["href"]
        jobs.append({"title": title, "company": company, "link": link})
    
    return jobs

print(scrape_indeed_jobs())