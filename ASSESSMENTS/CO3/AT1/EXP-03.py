import re
import math
from collections import Counter

# -----------------------------------------
# Training corpus
# -----------------------------------------

training = """
the student is studying artificial intelligence
the student is learning machine learning
the student is reading a book
the teacher is teaching artificial intelligence
machine learning is an important field
artificial intelligence is a growing field
"""

# -----------------------------------------
# Test corpus
# -----------------------------------------

test = [
    "the student is learning",
    "the teacher is teaching",
    "machine learning is important",
    "the student likes programming"
]


# -----------------------------------------
# Tokenization
# -----------------------------------------

def tokenize(text):
    return re.findall(r'\b[a-z]+\b', text.lower())


train_sentences = [
    tokenize(s)
    for s in re.split(r'[.!?]+', training)
    if tokenize(s)
]


# -----------------------------------------
# Counts
# -----------------------------------------

unigram = Counter()
bigram = Counter()
trigram = Counter()

for words in train_sentences:

    unigram.update(words)

    for i in range(len(words)-1):
        bigram[(words[i], words[i+1])] += 1

    for i in range(len(words)-2):
        trigram[
            (words[i], words[i+1], words[i+2])
        ] += 1


total = sum(unigram.values())


# -----------------------------------------
# Probability
# -----------------------------------------

def unigram_probability(word):

    return unigram[word] / total


def bigram_probability(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# -----------------------------------------
# Entropy
# -----------------------------------------

def calculate_entropy(sentence, n):

    words = tokenize(sentence)

    log_probability = 0
    count = 0

    for i in range(len(words)):

        if n == 1:
            p = unigram_probability(words[i])

        elif n == 2:

            if i == 0:
                p = unigram_probability(words[i])
            else:
                p = bigram_probability(
                    words[i-1],
                    words[i]
                )

        else:

            if i < 2:
                p = unigram_probability(words[i])

            else:
                p = trigram_probability(
                    words[i-2],
                    words[i-1],
                    words[i]
                )

        if p > 0:
            log_probability += -math.log2(p)
        else:
            # Unseen event
            log_probability += 20

        count += 1

    return log_probability / count


# -----------------------------------------
# Evaluation
# -----------------------------------------

for sentence in test:

    print("\nSentence:", sentence)

    for n in [1, 2, 3]:

        entropy = calculate_entropy(
            sentence,
            n
        )

        print(
            f"N={n} Entropy = {entropy:.4f}"
        )
