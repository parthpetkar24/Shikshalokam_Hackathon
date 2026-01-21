# Features/policy/policy_retriever.py

from Features.nlp.config import CANONICAL_ISSUES


class PolicyRetriever:
    """
    Retrieves relevant policy documents using canonical issue definitions.
    Single source of truth: CANONICAL_ISSUES
    """

    def __init__(self, documents: list):
        self.documents = documents

    def retrieve(self, issue_keys: list, top_k=1):
        """
        Args:
            issue_keys (list): canonical issue keys (e.g. 'student_absenteeism')
            top_k (int): number of documents to return

        Returns:
            list: matched policy documents
        """

        # 🔹 Collect keywords from canonical issues
        keywords = set()

        for issue_name, issue_data in CANONICAL_ISSUES.items():
            if issue_data["key"] in issue_keys:
                keywords.update(issue_data["variants"])

        # 🔥 HARD FALLBACK (hackathon safe)
        if not keywords:
            keywords = {"teacher", "training", "professional development"}

        matches = []

        for doc in self.documents:
            text = doc.get("text", "")

            if sum(1 for k in keywords if k in text) >= 2:
                matches.append(doc)

        return matches[:top_k]
