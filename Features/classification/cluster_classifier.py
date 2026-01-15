from nlp.config import CANONICAL_ISSUES, CLUSTER_METADATA
from collections import Counter

class ClusterClassifier:
    def __init__(self):
        pass

    def classify(self, canonical_issues: list):
        """
        Input: list of canonical issue strings
        Output: cluster classification result
        """

        if not canonical_issues:
            return {
                "cluster": None,
                "cluster_name": None,
                "issues": [],
                "message": "No recognizable issues found"
            }

        # Count cluster occurrences
        cluster_votes = []

        for issue in canonical_issues:
            if issue in CANONICAL_ISSUES:
                cluster_votes.append(
                    CANONICAL_ISSUES[issue]["cluster"]
                )

        if not cluster_votes:
            return {
                "cluster": None,
                "cluster_name": None,
                "issues": canonical_issues,
                "message": "Issues found but no cluster mapping available"
            }

        # Majority voting
        cluster = Counter(cluster_votes).most_common(1)[0][0]

        return {
            "cluster": cluster,
            "cluster_name": CLUSTER_METADATA[cluster]["name"],
            "issues": canonical_issues
        }
