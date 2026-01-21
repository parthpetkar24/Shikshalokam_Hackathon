from Features.microlearning.pdf_loader import PDFLoader
from Features.microlearning.text_cleanser import TextCleaner
from Features.microlearning.summarizer import RuleBasedSummarizer
from Features.microlearning.module_formatter import MicroModuleFormatter
from pathlib import Path


class ModuleGenerator:
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    def generate(self) -> dict:
        raw_text = PDFLoader.load_pdf(self.pdf_path)

        if isinstance(raw_text, bytes):
            raw_text = raw_text.decode("utf-8", errors="ignore")

        cleaned_text = TextCleaner.clean(raw_text)
        summary = RuleBasedSummarizer.summarize(cleaned_text)
        module = MicroModuleFormatter.format(summary)

        return {
            "summary": summary[:500],
            "duration": "10-15 minutes",
            "source": self.pdf_path.name,
            "module": module
        }
