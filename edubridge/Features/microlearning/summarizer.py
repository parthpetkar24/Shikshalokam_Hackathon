
class RuleBasedSummarizer:
    @staticmethod
    def summarize(text: str, max_words: int = 180) -> str:
        words = text.split()
        if len(words) <= max_words:
            return text
        return " ".join(words[:max_words]) + "..."
