# Constraint-Based Dialog Generation

responses = [
    "You have an exam tomorrow, so take a short break and then focus on one topic at a time; this will help you feel confident. You can make good progress by studying calmly and consistently.",

    "Because your exam is tomorrow, take a short break, return with a clear focus, and remind yourself that you can be confident after steady revision. You do not need to study everything at once.",

    "You may not concentrate right now, so take a short break and focus on a small study goal; finishing it can make you feel confident. Keep going step by step, because consistent effort will help you prepare for the exam."
]

required_words = ["focus", "break", "confident"]

print("Generated Responses")
print("=" * 60)

for i, response in enumerate(responses, 1):
    words_found = [
        word for word in required_words
        if word in response.lower()
    ]

    sentences = response.count(".") + response.count("!")

    print(f"\nResponse {i}:")
    print(response)
    print("Required keywords:", words_found)
    print("Sentence count:", sentences)
