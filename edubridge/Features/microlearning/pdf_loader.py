import pdfplumber
from pathlib import Path

class PDFLoader:
    @staticmethod
    def load_pdf_text(pdf_path: Path, skip_pages: int = 2) -> str:
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        pages = []
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                if i < skip_pages:
                    continue
                text = page.extract_text()
                if text:
                    pages.append(text)

        return "\n".join(pages)
