# microlearning/text_cleaner.py

import re

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"•", "", text)
        text = re.sub(r"\n+", " ", text)
        return text.strip()
