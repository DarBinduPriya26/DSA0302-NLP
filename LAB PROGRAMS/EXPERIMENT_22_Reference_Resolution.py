import re

text = input("Enter a text: ")

sentences = re.split(r'[.!?]', text)

last_male = None
last_female = None
last_entity = None

male_names = ["ravi", "arun", "john", "ram"]
female_names = ["sita", "mary", "anita"]

for sentence in sentences:
    words = sentence.strip().split()

    for word in words:
        clean = word.strip(",").lower()

        if clean in male_names:
            last_male = word
            last_entity = word

        elif clean in female_names:
            last_female = word
            last_entity = word

        elif clean in ["he", "him", "his"] and last_male:
            print(word, "->", last_male)

        elif clean in ["she", "her", "hers"] and last_female:
            print(word, "->", last_female)

        elif clean in ["it", "its"] and last_entity:
            print(word, "->", last_entity)