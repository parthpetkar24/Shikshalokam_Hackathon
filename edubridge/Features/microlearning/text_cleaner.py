import re

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"ISBN.*?\d+", "", text, flags=re.I)
        text = re.sub(r"ALL RIGHTS RESERVED.*", "", text, flags=re.I)
        text = re.sub(r"©.*?\d{4}", "", text)
        return text.strip()
