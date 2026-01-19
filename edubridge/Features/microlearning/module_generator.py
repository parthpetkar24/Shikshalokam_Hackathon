from pathlib import Path
from Features.microlearning.pdf_loader import PDFLoader
from Features.microlearning.text_cleanser import TextCleaner
from Features.microlearning.summarizer import RuleBasedSummarizer
from Features.microlearning.module_formatter import MicroModuleFormatter
import os
from django.conf import settings 


class ModuleGenerator:
    def __init__(self, topic: str):
        self.topic = topic
        self.pdf_path = os.path.join(
            settings.BASE_DIR,
            "data",
            "Guidelines50HoursCpd.pdf"
        )

    def generate(self) -> dict:
        raw_text = PDFLoader.load_pdf(self.pdf_path)

        if isinstance(raw_text, bytes):
            raw_text = raw_text.decode("utf-8", errors="ignore")

        cleaned_text = TextCleaner.clean(raw_text)
        summary = RuleBasedSummarizer.summarize(cleaned_text)
        module = MicroModuleFormatter.format(summary)

        return {
            "topic": self.topic,
            "summary": summary[:500],
            "duration": "10 minutes",
            "source": "Guidelines50HoursCpd.pdf"
        }
