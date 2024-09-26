import re
from collections import Counter

# List of common data science skills that we will match to the data we extract
common_skills = [
    "Python", "R", "SQL", "Java", "Javascript", "HTML", "GIT", "Machine Learning", 
    "Data Analysis", "Linux", "Data Visualization", "Deep Learning", "Pandas", "C#",
    "NumPy", "Cloud Computing", "Statistics", "Big Data", "IT", "Computer Engineering", 
    "Software Engineering", "Database Management", "Computer Science", "Backend", 
    "Information Technology", "Information Management", "Tableau", "Power BI", "C++",
    "Excel", "Data Engineering", "SAS", "MATLAB", "Applied Mathematics", "CSS", 
    "Agile", "Scrum", "Data Structures", "Algorithms", "API", "GraphQL", "Frontend",
    "Docker", "Kubernetes", "AWS", "Azure", "Software Development", "Testing",
    "Debugging", "Version Control", "Web Development", "Mobile Development",  
    "CI/CD", "Networking", "RDMS", "Oracle", "Postgres", "MySQL",  "Django","NoSQL",
    "OOP", "Node.js", "Agile", "Artificial Intelligence" 
]

# function that searches for the predefined skills in the description text
def extract_skills(description):
    found_skills = []
    for skill in common_skills:
        pattern = r'\b' + re.escape(skill) + r'\b' #ensure that any special characters in the skills are handled correctly.
        if re.search(pattern, description, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

# function that analyzes skills and their counts
def analyze_skills(skills):
    skill_counts = Counter(skills)
    return skill_counts.most_common()

