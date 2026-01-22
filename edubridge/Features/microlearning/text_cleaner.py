import re

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"ISBN.*?\d+", "", text, flags=re.I)
        text = re.sub(r"ALL RIGHTS RESERVED.*", "", text, flags=re.I)
        text = re.sub(r"\b\d{1,2}:\d{2}:\d{2}\b", "", text)
        text = re.sub(r"\b([A-Z])\s+([A-Z])\b", r"\1\2", text)
        return text.strip()
