import re

print("========== UNIVERSITY REGISTRATION ==========")

reg = input("Enter Register Number : ")
email = input("Enter Institutional Email : ")
course = input("Enter Course Code : ")
semester = input("Enter Semester : ")
mobile = input("Enter Mobile Number : ")

status = True

# Register Number
if re.fullmatch(r"\d{2}[A-Z]{3}\d{4}", reg):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False

# Email
if re.fullmatch(r"[A-Za-z0-9._%+-]+@university\.edu", email):
    print("Email : Valid")
else:
    print("Email : Invalid")
    status = False

# Course Code
if re.fullmatch(r"[A-Z]{2,4}\d{3}", course):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    status = False

# Semester
if re.fullmatch(r"[1-8]", semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    status = False

# Mobile
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    status = False

print("\n========== REGISTRATION STATUS ==========")

if status:
    print("Registration Successful")
else:
    print("Registration Failed")

