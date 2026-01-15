from keyword_model import KeywordExtractor
from cluster_classifier import ClusterClassifier

text = "Teachers need advanced teaching learning materials."

# Task 1
keyword_model = KeywordExtractor()
canonical_keywords = keyword_model.extract_keywords(text)

print("Canonical Issues:", canonical_keywords)

# Task 2
classifier = ClusterClassifier()
result = classifier.classify(canonical_keywords)

print("Cluster Result:", result)
