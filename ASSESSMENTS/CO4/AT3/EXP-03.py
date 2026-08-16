import nltk
import spacy
from nltk import CFG, PCFG
from nltk.parse import ChartParser, ViterbiParser

# -----------------------------------------
# Input Sentence
# -----------------------------------------
sentence = "She saw the man with a telescope".split()

print("SENTENCE:")
print(" ".join(sentence))

# -----------------------------------------
# 1. CFG PARSING
# -----------------------------------------
cfg_grammar = CFG.fromstring("""
S -> NP VP
NP -> Pronoun
NP -> Det N
NP -> Det N PP
VP -> V NP
VP -> V NP PP
PP -> P NP

Pronoun -> 'She'
Det -> 'the' | 'a'
N -> 'man' | 'telescope'
V -> 'saw'
P -> 'with'
""")

cfg_parser = ChartParser(cfg_grammar)

print("\nCFG PARSE TREES:")

count = 0

for tree in cfg_parser.parse(sentence):
    print(tree)
    count += 1

print("\nNumber of CFG parses:", count)

# -----------------------------------------
# 2. PCFG PARSING
# -----------------------------------------
pcfg_grammar = PCFG.fromstring("""
S -> NP VP [1.0]

NP -> Pronoun [0.2]
NP -> Det N [0.5]
NP -> Det N PP [0.3]

VP -> V NP [0.6]
VP -> V NP PP [0.4]

PP -> P NP [1.0]

Pronoun -> 'She' [1.0]

Det -> 'the' [0.6]
Det -> 'a' [0.4]

N -> 'man' [0.6]
N -> 'telescope' [0.4]

V -> 'saw' [1.0]

P -> 'with' [1.0]
""")

pcfg_parser = ViterbiParser(pcfg_grammar)

print("\nPCFG MOST PROBABLE PARSE:")

pcfg_trees = list(pcfg_parser.parse(sentence))

if pcfg_trees:
    best_tree = pcfg_trees[0]
    print(best_tree)
    print("Probability:", best_tree.prob())
else:
    print("No PCFG parse found.")

# -----------------------------------------
# 3. NEURAL DEPENDENCY PARSING
# -----------------------------------------
print("\nNEURAL DEPENDENCY PARSING:")

try:
    nlp = spacy.load("en_core_web_sm")

    doc = nlp("She saw the man with a telescope")

    for token in doc:
        print(
            token.text,
            "->",
            token.dep_,
            "->",
            token.head.text
        )

except OSError:
    print("spaCy English model is not installed.")
    print("Please run:")
    print("python -m spacy download en_core_web_sm")
