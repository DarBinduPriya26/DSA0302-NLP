singular_subjects = [
    "he", "she", "it", "boy", "girl", "student"
]

plural_subjects = [
    "they", "we", "boys", "girls", "students"
]

singular_verbs = [
    "is", "was", "plays", "runs", "likes"
]

plural_verbs = [
    "are", "were", "play", "run", "like"
]

sentence = input("Enter a sentence: ").lower().split()

if len(sentence) < 2:
    print("Please enter at least a subject and a verb.")
else:
    subject = sentence[0]
    verb = sentence[1]

    if subject in singular_subjects and verb in singular_verbs:
        print("Agreement is correct.")

    elif subject in plural_subjects and verb in plural_verbs:
        print("Agreement is correct.")

    else:
        print("Agreement is incorrect.")