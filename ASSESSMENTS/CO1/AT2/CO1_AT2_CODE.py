import re

# Input Text
text = """
Name: Bindu
Email: bindupriya@gmail.com
Alternate Email: bindu123@yahoo.com
Phone: 9876543210
Alternate Phone: 9123456789
Date of Birth: 15/08/2005
Website: https://www.binduportfolio.com
"""

print("INPUT TEXT")
print("----------------------------")
print(text)

# Regular Expression Patterns
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
phone_pattern = r'\b[6-9]\d{9}\b'
date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
website_pattern = r'https?://[^\s]+'

# Extract Information
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
dates = re.findall(date_pattern, text)
websites = re.findall(website_pattern, text)

# Display Output
print("\nOUTPUT")
print("----------------------------")

print("\nName:")
print("Bindu")

print("\nEmails Found:")
for email in emails:
    print(email)

print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)

print("\nDate Found:")
for date in dates:
    print(date)

print("\nWebsite Found:")
for website in websites:
    print(website)
