from signals import extract_keyword_signals
from rules import metadata_rules
from nlp_adapter import NLPAdapter
from collections import defaultdict

class ClusterClassifier:
    def __init__(self):
        self.nlp = NLPAdapter()

    def classify(self, text: str, metadata: dict):
        scores = defaultdict(float)
        reasons = defaultdict(list)

        # 1. Keyword signals
        keyword_signals = extract_keyword_signals(text)
        for s in keyword_signals:
            scores[s["cluster"]] += s["weight"]
            reasons[s["cluster"]].append(s["signal"])

        # 2. Metadata rules
        meta_signals = metadata_rules(metadata)
        for r in meta_signals:
            scores[r["cluster"]] += r["weight"]
            reasons[r["cluster"]].append(r["reason"])

        # 3. NLP model (currently empty)
        nlp_results = self.nlp.analyze(text)
        for res in nlp_results:
            scores[res["cluster"]] += res["confidence"]

        # 4. Decision
        if not scores:
            return {"cluster": "Unknown", "confidence": 0.0, "reasons": []}

        best_cluster = max(scores, key=scores.get)
        confidence = min(scores[best_cluster], 1.0)

        return {
            "cluster": best_cluster,
            "confidence": round(confidence, 2),
            "reasons": reasons[best_cluster]
        }
