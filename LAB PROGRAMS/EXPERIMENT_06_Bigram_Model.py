import random

# Input sentence
text = input("Enter a sentence: ").lower()

words = text.split()

# Create bigram dictionary
bigram = {}

for i in range(len(words) - 1):
    current = words[i]
    next_word = words[i + 1]

    if current not in bigram:
        bigram[current] = []

    bigram[current].append(next_word)

# Starting word
start = input("Enter the starting word: ").lower()

if start not in bigram:
    print("Starting word not found.")
else:
    result = [start]
    current = start

    for i in range(10):
        if current in bigram:
            next_word = random.choice(bigram[current])
            result.append(next_word)
            current = next_word
        else:
            break

    print("\nGenerated Text:")
    print(" ".join(result))