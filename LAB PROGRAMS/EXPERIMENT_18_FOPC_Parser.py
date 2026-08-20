import re

expression = input("Enter a logical expression: ")

patterns = {
    "Universal Quantifier": r"^forall\s+\w+\s*\(.+\)$",
    "Existential Quantifier": r"^exists\s+\w+\s*\(.+\)$",
    "Predicate": r"^\w+\(\w+\)$",
    "Logical AND": r".+\s+AND\s+.+",
    "Logical OR": r".+\s+OR\s+.+",
    "Logical NOT": r"^NOT\s+.+"
}

found = False

for name, pattern in patterns.items():
    if re.match(pattern, expression, re.IGNORECASE):
        print("Expression Type:", name)
        found = True
        break

if not found:
    print("Expression does not match the supported FOPC patterns.")