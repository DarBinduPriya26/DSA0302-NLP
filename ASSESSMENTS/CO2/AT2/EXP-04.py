words = ["activate", "activation", "reactivation"]

print("{:<18} {:<10} {:<10} {:<10} {:<20} {:<18} {:<20}".format(
    "Word", "Prefix", "Root", "Suffix",
    "Derivational Seq", "Normalized", "Parsed Representation"))

for word in words:

    if word == "activate":
        prefix = "-"
        root = "active"
        suffix = "-ate"
        sequence = "active + ate"
        normalized = "active"

    elif word == "activation":
        prefix = "-"
        root = "active"
        suffix = "-ation"
        sequence = "active + ate + ion"
        normalized = "active"

    elif word == "reactivation":
        prefix = "re"
        root = "active"
        suffix = "-ation"
        sequence = "re + active + ate + ion"
        normalized = "active"

    parsed = prefix + " | " + root + " | " + suffix

    print("{:<18} {:<10} {:<10} {:<10} {:<20} {:<18} {:<20}".format(
        word, prefix, root, suffix,
        sequence, normalized, parsed))
