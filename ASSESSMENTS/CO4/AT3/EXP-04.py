# Function to check Subject-Verb Agreement
def check_agreement(subject, verb):
    singular_subjects = ["boy", "girl", "student"]
    singular_verbs = ["plays", "writes", "runs"]

    if subject in singular_subjects and verb in singular_verbs:
        return "Subject-verb agreement is correct"
    else:
        return "Subject-verb agreement is incorrect"


# Function to check Verb Argument Structure
def check_arguments(verb, arguments):
    frames = {
        "give": 3,
        "sleep": 1
    }

    required = frames.get(verb, 0)

    if len(arguments) == required:
        return "Verb argument structure is correct"
    else:
        return "Verb argument structure is incorrect"


# Test Subject-Verb Agreement
print("Subject-Verb Agreement:")
print(check_agreement("student", "writes"))

# Test Verb Argument Structure
print("\nVerb Argument Structure:")
print(check_arguments("give", ["she", "child", "book"]))
