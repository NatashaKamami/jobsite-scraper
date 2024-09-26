import re
from collections import Counter

# List of common data science skills that we will match to the data we extract
common_skills = [
    "Python", "R", "SQL", "Java", "Javascript", "HTML", "GIT", "Machine Learning", 
    "Data Analysis", "Linux", "Data Visualization", "Deep Learning", "Pandas", 
    "NumPy", "Cloud Computing", "Statistics", "Big Data", "IT", "Computer Engineering", 
    "Software Engineering", "Database Management", "Computer Science", 
    "Information Technology", "Information Management", "Tableau", "Power BI", 
    "Excel", "Data Engineering", "SAS", "MATLAB", "Applied Mathematics"
]

# function that searches for the predefined skills in the description text
def extract_skills(description):
    found_skills = []
    for skill in common_skills:
        pattern = r'\b' + skill + r'\b' 
        if re.search(pattern, description, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

# function that analyzes skills and their counts
def analyze_skills(skills):
    skill_counts = Counter(skills)
    return skill_counts.most_common()

