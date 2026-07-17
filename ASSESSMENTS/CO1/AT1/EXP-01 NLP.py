import re

# Sample Resume
resumes = [
"""
Name: D. Bindu Priya
Email: bindupriya@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""
]

# Required Skills
required_skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]

eligible = []

print("========== RESUME INFORMATION EXTRACTION ==========\n")

for resume in resumes:

    # Extract Name
    name = re.search(r"Name:\s*(.*)", resume)

    # Extract Email
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

    # Extract Mobile Number
    mobile = re.search(r"\b[6-9]\d{9}\b", resume)

    # Extract Experience
    experience = re.search(r"(\d+)\s*year", resume, re.IGNORECASE)

    # Extract Skills
    skills = []

    for skill in required_skills:
        if re.search(skill, resume, re.IGNORECASE):
            skills.append(skill)

    years = int(experience.group(1))

    # Display Candidate Profile
    print("Candidate Name :", name.group(1))
    print("Email          :", email.group())
    print("Mobile         :", mobile.group())
    print("Skills         :", ", ".join(skills))
    print("Experience     :", years, "Years")

    # Structured Summary
    print("\n----- Candidate Profile Summary -----")
    print("Name       :", name.group(1))
    print("Email      :", email.group())
    print("Mobile     :", mobile.group())
    print("Experience :", years, "Years")
    print("Skills     :", ", ".join(skills))

    # Eligibility Check
    if years >= 2 and "Python" in skills:
        eligible.append(name.group(1))

    print("-------------------------------------------")

# Display Eligible Candidates
print("\n========== ELIGIBLE CANDIDATES ==========")

if eligible:
    for candidate in eligible:
        print(candidate)
else:
    print("No eligible candidates found.")
