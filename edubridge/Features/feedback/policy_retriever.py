# feedback/policy_retriever.py

ISSUE_KEYWORDS = {
    "student_absenteeism": ["attendance", "dropout", "retention"],
    "parent_engagement": ["parent", "family", "community"],
    "classroom_discipline": ["discipline", "behavior"],
    "language_barrier": ["language", "mother tongue", "multilingual"],
    "advanced_teaching_materials": ["materials", "resources", "tlm"],
    "experiential_science_teaching": ["science", "practical", "experiment"]
}


class PolicyRetriever:
    def __init__(self, documents):
        self.documents = documents

    def retrieve(self, issue_keys: list, top_k=3):
        keywords = set()
        for key in issue_keys:
            keywords.update(ISSUE_KEYWORDS.get(key, []))

        results = []

        for doc in self.documents:
            text = doc["text"].lower()
            if any(k in text for k in keywords):
                results.append(doc)

        return results[:top_k]
