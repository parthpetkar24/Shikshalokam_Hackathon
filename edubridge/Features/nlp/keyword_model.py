from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from .preprocess import clean_text
from .config import EMBEDDING_MODEL, TOP_K_KEYWORDS, CANONICAL_ISSUES
from sklearn.metrics.pairwise import cosine_similarity
import spacy

nlp = spacy.load("en_core_web_sm")

class KeywordExtractor:
    def __init__(self):
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        self.kw_model = KeyBERT(model=self.embedding_model)
    
    def normalize_from_raw_text(self, text: str):
        detected = set()
        text = text.lower()

        for canonical, data in CANONICAL_ISSUES.items():
            for variant in data["variants"]:
                if variant in text:
                    detected.add(canonical)
                    break

        return list(detected)
   
    def normalize_to_canonical(self, phrases):
        detected = set()

        for phrase in phrases:
            phrase = phrase.lower()
            for canonical, data in CANONICAL_ISSUES.items():
                for variant in data["variants"]:
                    if variant in phrase:
                        detected.add(canonical)

        return list(detected)

    
    def is_valid_keyword(self, phrase):
        doc = nlp(phrase)
        # Keep noun-heavy phrases only
        noun_count = sum(1 for token in doc if token.pos_ in ["NOUN", "PROPN"])
        verb_count = sum(1 for token in doc if token.pos_ == "VERB")
        return noun_count >= verb_count

    def deduplicate(self, phrases, threshold=0.75):
        embeddings = self.embedding_model.encode(phrases)
        final = []

        for i, phrase in enumerate(phrases):
            if not final:
                final.append(phrase)
                continue

            sims = cosine_similarity(
                [embeddings[i]],
                self.embedding_model.encode(final)
            )
            if max(sims[0]) < threshold:
                final.append(phrase)

        return final

    def extract_keywords(self, text: str):
        canonical_from_text = self.normalize_from_raw_text(text)
        raw = self.kw_model.extract_keywords(
            text.lower(),
            keyphrase_ngram_range=(1, 3),
            stop_words="english",
            top_n=15
        )

        phrases = [kw[0] for kw in raw]
        phrases = [p for p in phrases if self.is_valid_keyword(p)]
        canonical_from_keywords = self.normalize_to_canonical(phrases)
        final_canonical = list(set(canonical_from_text + canonical_from_keywords))
        return final_canonical

