# Word Sense Disambiguation and Predicate Logic

sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

# Possible senses
senses = {
    "financial_bank": [
        "money", "loan", "account", "finance"
    ],
    "riverbank": [
        "river", "flood", "storm", "water"
    ]
}

context = ["river", "flooded", "storm"]

scores = {}

for sense, keywords in senses.items():
    score = sum(1 for word in context if word in keywords)
    scores[sense] = score

best_sense = max(scores, key=scores.get)

print("Original Sentence:")
print(sentence)

print("\nSense Scores:")
for sense, score in scores.items():
    print(sense, ":", score)

print("\nResolved Sense:")
print(best_sense)

print("\nPredicate Logic:")
print("location(riverbank, river)")
print("flood(riverbank)")
print("after(flood(riverbank), storm)")
print("saved(riverbank)")
print("cause(quick_action, saved(riverbank))")

print("\nTarget Sentence:")
print("The riverbank beside the river flooded after the storm, but quick action saved it.")
