import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords (run once)
nltk.download('stopwords')

from nltk.corpus import stopwords

# Text preprocessing function
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)

# Input documents (you can replace these with file input)
doc1 = """Wireless sensor networks consist of sensor nodes that communicate wirelessly."""
doc2 = """Wireless sensor networks are made up of sensor nodes which communicate using wireless technology."""

# Preprocess documents
doc1 = preprocess(doc1)
doc2 = preprocess(doc2)

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([doc1, doc2])

# Compute cosine similarity
similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

# Convert to percentage
plagiarism_percentage = similarity_score * 100

print(f"Plagiarism Similarity: {plagiarism_percentage:.2f}%")
