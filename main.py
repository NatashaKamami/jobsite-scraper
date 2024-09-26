# importing necessary libraries
import pandas as pd
from job_scraper import scrape_jobs, close_driver
from skills import analyze_skills

# Defining job listings URL for Data Science and software engineering roles in MyJobMag website
datascience_url = "https://www.myjobmag.co.ke/search/jobs?q=data+science&location=Nairobi"
software_url = "https://www.myjobmag.co.ke/search/jobs?q=software+engineering&location=Nairobi"

# Scrape jobs from the URLs
datascience_skills = scrape_jobs(datascience_url)
software_skills = scrape_jobs(software_url)

# Analyze data science skills
datascience_skill_analysis = analyze_skills(datascience_skills)
#print(datascience_skill_analysis)

# Analyze software engineering skills
software_skill_analysis = analyze_skills(software_skills)
#print(software_skill_analysis)

# Create a DataFrame to store the skills and their frequency of occurrence
datascience_skills_df = pd.DataFrame(datascience_skill_analysis, columns=["Top Skills", "Count"])
print(datascience_skills_df)

software_skills_df = pd.DataFrame(software_skill_analysis, columns=["Top Skills", "Count"])
print(software_skills_df)

# Save the data to CSV files
datascience_skills_df.to_csv("datascience_skills.csv", index=False, encoding="utf-8")
print("Scraping complete. Top skills have been saved to 'datascience_skills.csv'.")

software_skills_df.to_csv("software_skills.csv", index=False, encoding="utf-8")
print("Scraping complete. Top skills have been saved to 'software_skills.csv.csv'.")

# Close the driver
close_driver()
