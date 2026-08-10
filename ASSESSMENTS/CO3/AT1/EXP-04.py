import re
from collections import Counter

# =========================================================
# POS TAGGING SYSTEM
# Rule-Based + Stochastic + Transformation-Based
# =========================================================

# ---------------------------------------------------------
# 1. LEXICAL DICTIONARY
# Penn Treebank POS Tags
# ---------------------------------------------------------

lexicon = {
    # Determiners
    "the": "DT",
    "a": "DT",
    "an": "DT",

    # Pronouns
    "i": "PRP",
    "you": "PRP",
    "he": "PRP",
    "she": "PRP",
    "we": "PRP",
    "they": "PRP",

    # Nouns
    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "machine": "NN",
    "science": "NN",
    "programming": "NN",
    "intelligence": "NN",
    "field": "NN",

    # Verbs
    "study": "VB",
    "studies": "VBZ",
    "learn": "VB",
    "learns": "VBZ",
    "read": "VB",
    "reads": "VBZ",
    "like": "VB",
    "likes": "VBZ",
    "teach": "VB",
    "teaches": "VBZ",

    # Auxiliary verbs
    "is": "VBZ",
    "am": "VBP",
    "are": "VBP",
    "was": "VBD",
    "were": "VBD",

    # Adjectives
    "good": "JJ",
    "important": "JJ",
    "artificial": "JJ",
    "growing": "JJ",

    # Adverbs
    "quickly": "RB",
    "slowly": "RB",
    "carefully": "RB",

    # Prepositions
    "in": "IN",
    "on": "IN",
    "at": "IN",
    "with": "IN",
    "from": "IN",
    "to": "TO",

    # Conjunctions
    "and": "CC",
    "but": "CC",
    "or": "CC"
}


# =========================================================
# 2. RULE-BASED POS TAGGER
# =========================================================

def rule_based_tagger(sentence):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    result = []

    for word in words:

        # Dictionary lookup
        if word in lexicon:
            tag = lexicon[word]

        # Grammar / suffix rules
        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ous"):
            tag = "JJ"

        elif word.endswith("ful"):
            tag = "JJ"

        elif word.endswith("tion"):
            tag = "NN"

        elif word.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        result.append((word, tag))

    return result


# =========================================================
# 3. STOCHASTIC POS TAGGER
# =========================================================

# Training corpus with word-tag pairs
training_data = [
    ("the", "DT"),
    ("student", "NN"),
    ("is", "VBZ"),
    ("studying", "VBG"),
    ("machine", "NN"),
    ("learning", "NN"),

    ("the", "DT"),
    ("teacher", "NN"),
    ("is", "VBZ"),
    ("teaching", "VBG"),
    ("artificial", "JJ"),
    ("intelligence", "NN"),

    ("the", "DT"),
    ("student", "NN"),
    ("reads", "VBZ"),
    ("book", "NN"),

    ("the", "DT"),
    ("student", "NN"),
    ("likes", "VBZ"),
    ("programming", "NN"),

    ("students", "NNS"),
    ("learn", "VB"),
    ("quickly", "RB")
]


# Count word-tag combinations
word_tag_count = Counter()

# Count tags
tag_count = Counter()

# Count tag transitions
transition_count = Counter()

previous_tag = "<START>"

for word, tag in training_data:

    word_tag_count[(word, tag)] += 1
    tag_count[tag] += 1

    transition_count[(previous_tag, tag)] += 1

    previous_tag = tag


def stochastic_tag(word, previous_tag=None):

    candidates = []

    # Find possible tags for the word
    for (w, tag), count in word_tag_count.items():

        if w == word:

            # Emission probability
            emission_probability = (
                count / tag_count[tag]
            )

            # Transition probability
            if previous_tag is not None:

                transition_total = sum(
                    count
                    for (prev, t), count
                    in transition_count.items()
                    if prev == previous_tag
                )

                if transition_total > 0:
                    transition_probability = (
                        transition_count[
                            (previous_tag, tag)
                        ] / transition_total
                    )
                else:
                    transition_probability = 0

            else:
                transition_probability = 1

            # Combined probability
            probability = (
                emission_probability *
                transition_probability
            )

            candidates.append(
                (tag, probability)
            )

    # If word exists in training data
    if candidates:
        return max(
            candidates,
            key=lambda x: x[1]
        )[0]

    # Unknown words
    return "NN"


def stochastic_tagger(sentence):

    words = re.findall(
        r'\b[a-z]+\b',
        sentence.lower()
    )

    result = []

    previous_tag = "<START>"

    for word in words:

        tag = stochastic_tag(
            word,
            previous_tag
        )

        result.append(
            (word, tag)
        )

        previous_tag = tag

    return result


# =========================================================
# 4. TRANSFORMATION-BASED POS TAGGER
# =========================================================

def transformation_based_tagger(sentence):

    words = re.findall(
        r'\b[a-z]+\b',
        sentence.lower()
    )

    # -----------------------------------------------------
    # Step 1: Initial tagging
    # -----------------------------------------------------

    tags = []

    for word in words:

        if word in lexicon:
            tag = lexicon[word]

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        tags.append(tag)


    # -----------------------------------------------------
    # Step 2: Apply transformation rules
    # -----------------------------------------------------

    for i in range(1, len(words)):

        # -------------------------------------------------
        # Rule 1:
        # Pronoun + Noun -> Verb
        # Example:
        # I study
        # I -> PRP
        # study -> NN initially
        # study -> VB after transformation
        # -------------------------------------------------

        if tags[i - 1] == "PRP":
            if tags[i] == "NN":
                tags[i] = "VB"


        # -------------------------------------------------
        # Rule 2:
        # Auxiliary verb + Noun -> Verb
        # -------------------------------------------------

        if tags[i - 1] in ["VBZ", "VBP", "VBD"]:

            if tags[i] == "NN":
                tags[i] = "VB"


        # -------------------------------------------------
        # Rule 3:
        # Determiner + Verb -> Noun
        # Example:
        # the study
        # -------------------------------------------------

        if tags[i - 1] == "DT":

            if tags[i] == "VB":
                tags[i] = "NN"


        # -------------------------------------------------
        # Rule 4:
        # Adjective + Noun
        # -------------------------------------------------

        if tags[i - 1] == "JJ":

            if tags[i] == "VB":
                tags[i] = "NN"


    return list(zip(words, tags))


# =========================================================
# 5. USER INPUT
# =========================================================

sentence = input(
    "Enter an English sentence: "
)


# =========================================================
# 6. RULE-BASED OUTPUT
# =========================================================

print("\n" + "=" * 55)
print("RULE-BASED POS TAGGER")
print("=" * 55)

rule_result = rule_based_tagger(sentence)

for word, tag in rule_result:
    print(f"{word:15} -> {tag}")


# =========================================================
# 7. STOCHASTIC OUTPUT
# =========================================================

print("\n" + "=" * 55)
print("STOCHASTIC POS TAGGER")
print("=" * 55)

stochastic_result = stochastic_tagger(sentence)

for word, tag in stochastic_result:
    print(f"{word:15} -> {tag}")


# =========================================================
# 8. TRANSFORMATION-BASED OUTPUT
# =========================================================

print("\n" + "=" * 55)
print("TRANSFORMATION-BASED POS TAGGER")
print("=" * 55)

transformation_result = transformation_based_tagger(
    sentence
)

for word, tag in transformation_result:
    print(f"{word:15} -> {tag}")


# =========================================================
# 9. COMPARISON
# =========================================================

print("\n" + "=" * 70)
print("COMPARISON OF ALL THREE POS TAGGERS")
print("=" * 70)

print(
    f"{'WORD':15}"
    f"{'RULE':15}"
    f"{'STOCHASTIC':15}"
    f"{'TRANSFORMATION':15}"
)

print("-" * 70)

for i in range(len(rule_result)):

    word = rule_result[i][0]
    rule_tag = rule_result[i][1]
    stochastic_tag_value = stochastic_result[i][1]
    transformation_tag = transformation_result[i][1]

    print(
        f"{word:15}"
        f"{rule_tag:15}"
        f"{stochastic_tag_value:15}"
        f"{transformation_tag:15}"
    )
