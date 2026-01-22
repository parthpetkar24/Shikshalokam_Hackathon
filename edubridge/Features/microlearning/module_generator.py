from Features.microlearning.pdf_loader import PDFLoader
from Features.microlearning.text_cleaner import TextCleaner
from Features.microlearning.policy_extractor import PolicyExtractor
from Features.microlearning.transformer_summarizer import TransformerSummarizer

class ModuleGenerator:
    def __init__(self, pdf_path, policy_keywords, policy_intent, title):
        self.pdf_path = pdf_path
        self.policy_keywords = policy_keywords
        self.policy_intent = policy_intent
        self.title = title

    def generate(self) -> dict:
        raw_text = PDFLoader.load_pdf_text(self.pdf_path)
        cleaned_text = TextCleaner.clean(raw_text)

        relevant_policy = PolicyExtractor.extract_relevant_text(
            cleaned_text,
            self.policy_keywords
        )

        if not relevant_policy:
            relevant_policy = self.policy_intent

        summary = TransformerSummarizer.summarize(relevant_policy)

        return {
            "module_title": self.title,
            "policy_source": self.pdf_path.name,
            "learning_objectives": [
                f"Understand policy guidance on {self.title.lower()}",
                "Identify classroom-relevant practices",
                "Apply one CPD strategy",
                "Reflect on professional growth"
            ],
            "summary": summary,
            "duration": "10–15 minutes"
        }
