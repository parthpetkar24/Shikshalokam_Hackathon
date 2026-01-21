from Features.nlp.preprocess import normalize_text
from Features.nlp.config import CANONICAL_ISSUES


class KeywordExtractor:
    def extract_keywords(self, text: str):
        text = normalize_text(text)
        detected = []

        for name, data in CANONICAL_ISSUES.items():
            for variant in data["variants"]:
                if variant in text:
                    detected.append({
                        "name": name,
                        "key": data["key"],
                        "cluster": data["cluster"]
                    })
                    break

        return detected
