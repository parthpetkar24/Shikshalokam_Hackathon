# microlearning/pdf_loader.py

from pathlib import Path
import PyPDF2

class PDFLoader:
    @staticmethod
    def load_pdf(pdf_path: Path) -> str:
        text = ""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
