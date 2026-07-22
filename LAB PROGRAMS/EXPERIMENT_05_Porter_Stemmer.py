from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Get input from user
words = input("Enter words separated by space: ").split()

print("\nOriginal Word\tStemmed Word")
print("-" * 30)

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")