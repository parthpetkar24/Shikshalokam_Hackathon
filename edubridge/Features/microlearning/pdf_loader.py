import os
from pathlib import Path
import PyPDF2

class PDFLoader:
    @staticmethod
    def load_pdf(pdf_path):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found at: {pdf_path}")

        with open(pdf_path, "rb") as file:
            return file.read()
