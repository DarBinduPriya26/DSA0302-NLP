import re

# Get input from the user
text = input("Enter a sentence: ")
pattern = input("Enter the word to search: ")

# Search for the first occurrence
result = re.search(pattern, text, re.IGNORECASE)

if result:
    print("\nWord Found!")
    print("Matched Word :", result.group())
    print("Starting Position :", result.start())
    print("Ending Position :", result.end())
else:
    print("\nWord Not Found!")

# Find all occurrences
matches = re.findall(pattern, text, re.IGNORECASE)

print("\nTotal Occurrences :", len(matches))
print("Matched Words :", matches)