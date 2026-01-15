import re
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
STOP_WORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if token.text not in STOP_WORDS and token.is_alpha
    ]

    return " ".join(tokens)
