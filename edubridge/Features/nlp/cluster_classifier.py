from collections import Counter
from Features.nlp.config import CLUSTER_METADATA


class ClusterClassifier:
    def identify_cluster(self, canonical_issues: list) -> dict:

        if not canonical_issues:
            return {
                "cluster_id": "Unclassified",
                "cluster_name": "Not clearly identified",
                "confidence": 0.0,
                "issues": []
            }

        votes = Counter([i["cluster"] for i in canonical_issues])
        cluster_id, count = votes.most_common(1)[0]

        return {
            "cluster_id": cluster_id,
            "cluster_name": CLUSTER_METADATA[cluster_id]["name"],
            "confidence": round(count / len(canonical_issues), 2),
            "issues": canonical_issues
        }
