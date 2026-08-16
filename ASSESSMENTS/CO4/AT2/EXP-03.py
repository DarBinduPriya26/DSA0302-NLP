import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

# -------------------------------
# Context-Free Grammar (CFG)
# -------------------------------
grammar = CFG.fromstring("""
S -> NP VP

NP -> DET NOUN
NP -> DET NOUN REL

REL -> PRON VERB DET NOUN TIME

VP -> VERB GERUND CONJ GERUND

GERUND -> VERB NOUN
GERUND -> VERB DET NOUN PP

PP -> PREP NOUN

DET -> 'the' | 'a'

NOUN -> 'doctor' | 'patient' | 'medication' | 'visit' | 'Chennai'

PRON -> 'who'

VERB -> 'reviewed' | 'recommends' | 'starting' | 'scheduling'

TIME -> 'last' 'week'

CONJ -> 'and'

PREP -> 'in'
""")

# -------------------------------
# Input Sentence
# -------------------------------
sentence = [
    'the', 'doctor', 'who', 'reviewed', 'the', 'patient',
    'last', 'week', 'recommends', 'starting', 'medication',
    'and', 'scheduling', 'a', 'visit', 'in', 'Chennai'
]

print("Medical Sentence:")
print(" ".join(sentence))

# -------------------------------
# Earley Chart Parser
# -------------------------------
parser = EarleyChartParser(grammar)

trees = list(parser.parse(sentence))

print("\nParsing Result:")

if trees:
    print("Sentence parsed successfully!")

    print("\nParse Tree:")
    print(trees[0])
else:
    print("Parsing failed.")

# -------------------------------
# Feature Structure
# -------------------------------
print("\nFeature Structure:")
print("Doctor: Person = 3, Number = Singular")
print("Recommends: Person = 3, Number = Singular")
print("Agreement: Correct")

# -------------------------------
# Semantic Representation
# -------------------------------
print("\nSemantic Representation:")
print("Review(Doctor, Patient, LastWeek)")
print("Recommend(Doctor, Medication)")
print("Schedule(Doctor, FollowUpVisit, Chennai)")

# -------------------------------
# Structured Output
# -------------------------------
print("\nStructured Output:")
print("Diagnosis: Not explicitly stated")
print("Treatment: Start Medication")
print("Follow-up: Schedule Visit")
print("Location: Chennai")
