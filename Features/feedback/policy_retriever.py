CLUSTER_KEYWORDS = {
    "A": ["attendance", "discipline", "behaviour", "behavior", "engagement"],
    "B": ["experiential", "activity", "science", "critical thinking", "tlm"],
    "C": ["language", "multilingual", "mother tongue", "local context"]
}

class PolicyRetriever:
    def __init__(self, documents):
        self.documents = documents

    def retrieve(self, cluster: str, top_k=3):
        keywords = CLUSTER_KEYWORDS.get(cluster, [])
        results = []

        for doc in self.documents:
            text = doc["text"].lower()
            if any(k in text for k in keywords):
                results.append(doc)

        return results[:top_k]
