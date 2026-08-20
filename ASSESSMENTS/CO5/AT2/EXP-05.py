# Q5 - Interlingua Based Statistical Machine Translation

def machine_translation():
    print("INTERLINGUA + STATISTICAL MACHINE TRANSLATION")
    print("-" * 50)

    # Step 1: Source sentence
    source = "The boy is playing football."

    print("STEP 1: SOURCE SENTENCE ANALYSIS")
    print("--------------------------------")
    print("Source:", source)

    print("\nTokens:")
    print("The -> Article")
    print("boy -> Agent")
    print("is playing -> Present Continuous Action")
    print("football -> Object")

    # Step 2: Interlingua representation
    print("\nSTEP 2: INTERLINGUA REPRESENTATION")
    print("----------------------------------")

    interlingua = {
        "Agent": "Boy",
        "Action": "Play",
        "Object": "Football",
        "Tense": "Present",
        "Aspect": "Continuous"
    }

    for key, value in interlingua.items():
        print(key, "=", value)

    # Step 3: Candidate translations
    print("\nSTEP 3: CANDIDATE TRANSLATIONS")
    print("--------------------------------")

    candidates = {
        "T1": "लड़का फुटबॉल खेल रहा है।",
        "T2": "लड़का फुटबॉल खेलता है।",
        "T3": "लड़का फुटबॉल खेल रहा था।"
    }

    for key, value in candidates.items():
        print(key, ":", value)

    # Step 4: Statistical scoring
    print("\nSTEP 4: STATISTICAL SCORING")
    print("----------------------------")

    scores = {
        "T1": 0.92,
        "T2": 0.65,
        "T3": 0.28
    }

    for key, score in scores.items():
        print(key, "Score =", score)

    best_candidate = max(scores, key=scores.get)

    print("\nHighest Scoring Candidate:")
    print(best_candidate)
    print("Score =", scores[best_candidate])

    # Step 5: Final translation
    print("\nSTEP 5: FINAL TRANSLATION")
    print("--------------------------")

    final_translation = candidates[best_candidate]

    print("Source Sentence:")
    print(source)

    print("\nFinal Translated Sentence:")
    print(final_translation)

    # Validation
    print("\nVALIDATION")
    print("----------")
    print("Agent    : Boy -> लड़का")
    print("Action   : Playing -> खेल रहा है")
    print("Object   : Football -> फुटबॉल")
    print("Tense    : Present")
    print("Aspect   : Continuous")

    print("\nConclusion:")
    print("The Interlingua preserves the meaning of the source sentence.")
    print("Statistical scoring selects the most appropriate translation.")
    print("The hybrid approach reduces ambiguity and improves translation quality.")


machine_translation()
