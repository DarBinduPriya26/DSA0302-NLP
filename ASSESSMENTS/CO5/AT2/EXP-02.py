# Q2 - Text Coherence and Discourse Structure

def analyze_coherence():
    print("TEXT COHERENCE AND DISCOURSE STRUCTURE")
    print("-" * 45)

    sentences = [
        "The roads were flooded after heavy rainfall.",
        "Therefore, schools were closed for the day.",
        "Students attended classes online."
    ]

    print("Input Discourse:\n")

    for i, sentence in enumerate(sentences, 1):
        print("S" + str(i) + ":", sentence)

    print("\nDiscourse Relations:")
    print("S1 -> S2 : CAUSE-EFFECT")
    print("S2 -> S3 : RESULT / SEQUENCE")

    print("\nDiscourse Structure:")
    print("Heavy rainfall")
    print("      |")
    print("      v")
    print("Roads were flooded")
    print("      |")
    print("      v")
    print("Schools were closed")
    print("      |")
    print("      v")
    print("Students attended classes online")

    print("\nCoherence Validation:")
    print("1. Heavy rainfall caused the roads to become flooded.")
    print("2. Flooded roads resulted in school closure.")
    print("3. School closure led students to attend classes online.")
    print("4. The logical sequence maintains coherence.")


analyze_coherence()
