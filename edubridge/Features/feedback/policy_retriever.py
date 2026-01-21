class PolicyRetriever:
    def __init__(self, documents):
        self.documents = documents

    def retrieve(self, issue_keys, top_k=1):
        if not issue_keys:
            print("POLICY MATCH MODE: FALLBACK")
            return self.documents[:top_k]

        print("POLICY MATCH MODE: ISSUE-BASED")

        matched = []
        for doc in self.documents:
            for key in issue_keys:
                if key.replace("_", " ") in doc["text"]:
                    matched.append(doc)
                    break

        return matched[:top_k] if matched else self.documents[:top_k]
