# importing necessary libraries
import pandas as pd
from job_scraper import scrape_jobs, close_driver
from skills import analyze_skills

# Defining job listings URL for Data Science roles in MyJobMag website
url = "https://www.myjobmag.co.ke/search/jobs?q=data+science&location=Nairobi"
 
# Scrape jobs from the URL
all_skills = scrape_jobs(url)

# Analyze skills
skill_analysis = analyze_skills(all_skills)
print(skill_analysis)

# Create a DataFrame to store the skills and their frequency of occurrence
skills_df = pd.DataFrame(skill_analysis, columns=["Top Skills", "Count"])
print(skills_df)

# Save the data to a CSV file
skills_df.to_csv("top_skills.csv", index=False, encoding="utf-8")
print("Scraping complete. Top skills have been saved to 'top_skills.csv'.")

# Close the driver
close_driver()
