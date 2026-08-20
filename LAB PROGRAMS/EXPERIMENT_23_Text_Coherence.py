import re
from collections import Counter

text = input("Enter a text: ")

sentences = [
    s.strip()
    for s in re.split(r'[.!?]', text)
    if s.strip()
]

if len(sentences) < 2:
    print("Enter at least two sentences.")
else:
    words = []

    for sentence in sentences:
        words.extend(
            re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
        )

    frequency = Counter(words)

    repeated_words = sum(
        1 for word, count in frequency.items()
        if count > 1
    )

    if len(frequency) > 0:
        score = (repeated_words / len(frequency)) * 100
    else:
        score = 0

    print("\nNumber of Sentences:", len(sentences))
    print("Repeated Key Words:", repeated_words)
    print(f"Coherence Score: {score:.2f}%")

    if score >= 30:
        print("Text shows good lexical coherence.")
    else:
        print("Text shows low lexical coherence.")