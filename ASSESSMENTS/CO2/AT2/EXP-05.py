words = ["create", "creates", "creating"]

print("{:<15} {:<10} {:<25} {:<12} {:<15} {:<15}".format(
    "Word", "Suffix",
    "Grammar Category", "Root",
    "Normalized", "Final Output"))

for word in words:

    if word == "create":
        suffix = "-"
        category = "Base Form"
        root = "create"
        normalized = "create"

    elif word == "creates":
        suffix = "-s"
        category = "Third Person Singular"
        root = "create"
        normalized = "create"

    elif word == "creating":
        suffix = "-ing"
        category = "Present Participle"
        root = "create"
        normalized = "create"

    print("{:<15} {:<10} {:<25} {:<12} {:<15} {:<15}".format(
        word, suffix, category,
        root, normalized, normalized))
