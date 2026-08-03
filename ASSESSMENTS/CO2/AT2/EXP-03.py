words = ["govern", "government", "governance"]

print("{:<15} {:<12} {:<15} {:<20} {:<15} {:<15}".format(
    "Word", "Root", "Affix",
    "Derivational Level", "Normalized", "Final Output"))

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Base"
        normalized = "govern"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        level = "Level 1"
        normalized = "govern"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        level = "Level 1"
        normalized = "govern"

    print("{:<15} {:<12} {:<15} {:<20} {:<15} {:<15}".format(
        word, root, affix, level,
        normalized, normalized))
