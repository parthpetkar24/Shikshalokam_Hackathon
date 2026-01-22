import re

class PolicyExtractor:
    @staticmethod
    def extract_relevant_text(text: str, keywords: list[str], window: int = 600) -> str:
        extracted = []

        for keyword in keywords:
            pattern = re.compile(
                rf"(.{{0,{window}}}\b{re.escape(keyword)}\b.{{0,{window}}})",
                re.IGNORECASE
            )
            matches = pattern.findall(text)
            extracted.extend(matches)

        return " ".join(set(extracted))
