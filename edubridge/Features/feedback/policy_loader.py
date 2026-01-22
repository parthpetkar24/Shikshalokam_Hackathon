import os
from PyPDF2 import PdfReader


class PolicyLoader:
    def __init__(self, pdf_paths: list):
        self.pdf_paths = pdf_paths

    def load(self) -> list:
        documents = []

        for path in self.pdf_paths:
            if not os.path.exists(path):
                continue

            try:
                reader = PdfReader(path)
                full_text = ""

                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + " "

                documents.append({
                    "source": os.path.basename(path),
                    "text": full_text.lower()
                })

            except Exception:
                continue

        return documents
