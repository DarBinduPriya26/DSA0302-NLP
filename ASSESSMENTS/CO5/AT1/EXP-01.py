# Constraint-Based Coreference Resolution

mentions = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["ball", "park"],
    "him": ["John", "Mary", "dog"],
    "they": ["John", "Mary", "dog"]
}

resolved = {
    "He": "John",
    "She": "Mary",
    "it": "ball",
    "him": "John",
    "they": "John + Mary + dog"
}

print("COREference Resolution")
print("-" * 45)

for mention, candidates in mentions.items():
    print(f"{mention}: {candidates}")
    print(f"Resolved antecedent: {resolved[mention]}")
    print()

print("Final Coreference Chains")
print("John -> He -> him -> they")
print("Mary -> She -> they")
print("ball -> it")
print("dog -> they")
