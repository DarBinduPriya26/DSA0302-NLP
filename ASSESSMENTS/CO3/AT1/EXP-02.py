import re
from collections import Counter

corpus = """
the student is studying artificial intelligence
the student is learning machine learning
the student is reading a book
the student likes programming
the teacher is teaching artificial intelligence
the teacher likes machine learning
machine learning is an important field
artificial intelligence is a growing field
the student is interested in artificial intelligence
"""

sentences = re.split(r'[.!?]+', corpus.lower())

data = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)

    if words:
        data.append(["<s>"] + words + ["</s>"])

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in data:

    unigram.update(sentence)

    for i in range(len(sentence)-1):
        bigram[(sentence[i], sentence[i+1])] += 1

    for i in range(len(sentence)-2):
        trigram[
            (sentence[i], sentence[i+1], sentence[i+2])
        ] += 1


total_words = sum(unigram.values())


# -----------------------------------------
# Probability functions
# -----------------------------------------

def P1(word):
    return unigram[word] / total_words


def P2(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def P3(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# -----------------------------------------
# Backoff
# -----------------------------------------

def backoff_probability(w1, w2, w3):

    trigram_prob = P3(w1, w2, w3)

    if trigram_prob > 0:
        return trigram_prob

    bigram_prob = P2(w2, w3)

    if bigram_prob > 0:
        return bigram_prob

    return P1(w3)


# -----------------------------------------
# Deleted Interpolation
# -----------------------------------------

lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.5


def interpolation_probability(w1, w2, w3):

    return (
        lambda1 * P1(w3)
        + lambda2 * P2(w2, w3)
        + lambda3 * P3(w1, w2, w3)
    )


# -----------------------------------------
# Prediction
# -----------------------------------------

def predict(query, method):

    words = re.findall(r'\b[a-z]+\b', query.lower())

    if len(words) < 2:
        return []

    w1 = words[-2]
    w2 = words[-1]

    predictions = []

    vocabulary = [
        word for word in unigram
        if word not in ["<s>", "</s>"]
    ]

    for word in vocabulary:

        if method == "unsmoothed":
            probability = P3(w1, w2, word)

        elif method == "backoff":
            probability = backoff_probability(
                w1, w2, word
            )

        else:
            probability = interpolation_probability(
                w1, w2, word
            )

        predictions.append((word, probability))

    return sorted(
        predictions,
        key=lambda x: x[1],
        reverse=True
    )[:5]


# -----------------------------------------
# User Input
# -----------------------------------------

query = input("Enter sentence/query: ")

for method in ["unsmoothed", "backoff", "interpolation"]:

    print("\n", method.upper())

    results = predict(query, method)

    for word, probability in results:
        print(
            f"{word:15} {probability:.4f}"
        )
