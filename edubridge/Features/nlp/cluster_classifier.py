# nlp/cluster_classifier.py

from collections import Counter
from Features.nlp.config import CLUSTER_METADATA


class ClusterClassifier:
    def identify_cluster(self, canonical_issues: list) -> dict:

        if not canonical_issues:
            return {
                "cluster_id": "Insufficient data",
                "cluster_name": "Not clearly identified",
                "confidence": 0.0,
                "issues": [],
                "message": "No recognizable issues found"
            }

        cluster_votes = [item["cluster"] for item in canonical_issues]

        vote_counter = Counter(cluster_votes)
        cluster_id, vote_count = vote_counter.most_common(1)[0]

        confidence = round(vote_count / len(cluster_votes), 2)

        return {
            "cluster_id": cluster_id,
            "cluster_name": CLUSTER_METADATA[cluster_id]["name"],
            "confidence": confidence,
            "issues": canonical_issues,
            "message": "Cluster identified successfully"
        }
