from transformers import pipeline

class TransformerSummarizer:
    """
    Singleton Transformer summarizer using BART
    """

    _summarizer = None

    @classmethod
    def get_model(cls):
        if cls._summarizer is None:
            cls._summarizer = pipeline(
                "summarization",
                model="facebook/bart-large-cnn",
                device=-1  # CPU
            )
        return cls._summarizer

    @classmethod
    def summarize(cls, text: str) -> str:
        summarizer = cls.get_model()

        # BART input limit protection
        text = text[:3000]

        summary = summarizer(
            text,
            max_length=180,
            min_length=80,
            do_sample=False
        )

        return summary[0]["summary_text"]
