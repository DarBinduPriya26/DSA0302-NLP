words = ["analyzing", "analysis", "analytical"]

print("{:<15} {:<12} {:<12} {:<15} {:<15}".format(
    "Word", "Root", "Affix", "Type", "Normalized"))

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        mtype = "Inflectional"
        normalized = "analyze"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        mtype = "Derivational"
        normalized = "analyze"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        mtype = "Derivational"
        normalized = "analyze"

    print("{:<15} {:<12} {:<12} {:<15} {:<15}".format(
        word, root, affix, mtype, normalized))
