from transformers import pipeline

class TransformerSummarizer:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = pipeline(
                "summarization",
                model="facebook/bart-large-cnn",
                device=-1  # CPU
            )
        return cls._model

    @classmethod
    def summarize(cls, text: str) -> str:
        model = cls.get_model()

        # Safety trim
        text = text[:3000]

        input_length = len(text.split())

        # 🧠 Dynamic length control (THIS FIXES THE WARNING)
        max_length = max(40, int(input_length * 0.6))
        min_length = max(20, int(input_length * 0.3))

        # If text is already short, don't over-summarize
        if input_length < 80:
            return text

        summary = model(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )

        return summary[0]["summary_text"]
