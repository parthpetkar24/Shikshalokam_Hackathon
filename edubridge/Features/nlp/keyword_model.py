from Features.nlp.preprocess import normalize_text
from .config import CANONICAL_ISSUES

class KeywordExtractor:

    def _detect_from_text(self, text: str):
        detected = []
        text = text.lower()

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

    def extract_keywords(self, text: str):
        text = normalize_text(text)

        canonical_from_text = self._detect_from_text(text)


        if canonical_from_text:
            return canonical_from_text

        return [{
        "name": "general classroom issue",
        "key": "student_absenteeism",
        "cluster": "A"
    }]
