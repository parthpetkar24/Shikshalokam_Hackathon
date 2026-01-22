import re

class PolicyExtractor:
    @staticmethod
    def extract(text: str, keywords: list[str], window=800) -> str:
        extracted = []

        for kw in keywords:
            pattern = re.compile(
                rf"(.{{0,{window}}}{re.escape(kw)}.{{0,{window}}})",
                re.IGNORECASE
            )
            matches = pattern.findall(text)
            extracted.extend(matches)

        return " ".join(extracted)
