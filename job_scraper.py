# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
from skills import extract_skills

# Setting up the web driver and specifying the path to your ChromeDriver
chrome_driver_path = "C:/chromedriver/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Scraping the job skills
def scrape_jobs(url):
    skills = []
    page = 1  # initial counter

    while page <= 10:  # Loop through the first 10 pages
        url = f"{url}&page={page}"  # Update URL for pagination
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        job_listings = soup.find_all("li", class_="job-list-li")
        if not job_listings:  # If there are no job listings, break the loop
            break
        
        for job in job_listings:
            h2_tag = job.find("h2")  # Get the <h2> tag within the job listing
            if h2_tag:  # Check if <h2> exists
                link_tag = h2_tag.find("a")  # Get the first <a> tag within the <h2> tag
                if link_tag:
                    link = link_tag["href"]  # Extract the href attribute
                    if link:
                        if link.startswith("/"):
                            link = "https://www.myjobmag.co.ke" + link
                        result = requests.get(link)
                        if result.status_code == 200:
                            html = result.content
                            desc_soup = BeautifulSoup(html, 'html.parser')
                            elements = desc_soup.find("div", class_="job-details")
                            if elements:
                                descriptions = elements.find_all("li")
                                if descriptions:
                                    for description in descriptions:
                                        text_description = description.get_text(strip=True)  # Clean whitespaces
                                        skills.extend(extract_skills(text_description)) 
        page += 1
    return skills

# function for quiting the driver
def close_driver():
    driver.quit()

