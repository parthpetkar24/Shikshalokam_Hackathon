from pathlib import Path

class PDFLoader:
    @staticmethod
    def load_pdf(pdf_path: Path):
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found at: {pdf_path}")

        with open(pdf_path, "rb") as file:
            return file.read()
