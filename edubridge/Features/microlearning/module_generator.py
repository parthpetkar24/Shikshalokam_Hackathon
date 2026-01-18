# microlearning/module_generator.py

from pathlib import Path
from microlearning.pdf_loader import PDFLoader
from microlearning.text_cleanser import TextCleaner
from microlearning.summarizer import RuleBasedSummarizer
from microlearning.module_formatter import MicroModuleFormatter

class ModuleGenerator:
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    def generate(self) -> dict:
        raw_text = PDFLoader.load_pdf(self.pdf_path)
        cleaned_text = TextCleaner.clean(raw_text)
        summary = RuleBasedSummarizer.summarize(cleaned_text)
        module = MicroModuleFormatter.format(summary)
        return module
