from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning is used in artificial intelligence.",
    "Natural language processing deals with text and language.",
    "Deep learning is a branch of machine learning.",
    "Python is widely used for machine learning."
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf_matrix)[0]

ranking = scores.argsort()[::-1]

print("\nDocument Ranking:")

for index in ranking:
    print(f"Document {index + 1}: Score = {scores[index]:.4f}")
    print(documents[index])
    print()