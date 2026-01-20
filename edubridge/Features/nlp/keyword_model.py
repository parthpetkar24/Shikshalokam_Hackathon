# nlp/keyword_model.py

from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

from .config import CANONICAL_ISSUES, EMBEDDING_MODEL

nlp = spacy.load("en_core_web_sm")


class KeywordExtractor:
    def __init__(self):
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        self.kw_model = KeyBERT(model=self.embedding_model)

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
        """
        FINAL NLP OUTPUT (authoritative):
        [
          {
            "name": "student absenteeism",
            "key": "student_absenteeism",
            "cluster": "A"
          }
        ]
        """

        canonical_from_text = self._detect_from_text(text)

        raw_keywords = self.kw_model.extract_keywords(
            text.lower(),
            keyphrase_ngram_range=(1, 3),
            stop_words="english",
            top_n=15
        )

        phrases = [kw[0] for kw in raw_keywords]
        canonical_from_keywords = []

        for phrase in phrases:
            canonical_from_keywords.extend(self._detect_from_text(phrase))

        # Deduplicate by key
        seen = {}
        for item in canonical_from_text + canonical_from_keywords:
            seen[item["key"]] = item

        return list(seen.values())
