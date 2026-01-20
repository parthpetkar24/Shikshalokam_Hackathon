# feedback/policy_loader.py
import fitz  # PyMuPDF
from pathlib import Path

class PolicyLoader:
    def __init__(self, pdf_paths, chunk_size=400):
        self.pdf_paths = pdf_paths
        self.chunk_size = chunk_size

    def _chunk_text(self, text: str):
        words = text.split()
        for i in range(0, len(words), self.chunk_size):
            yield " ".join(words[i:i + self.chunk_size])

    def load_documents(self):
        documents = []

        for path in self.pdf_paths:
            doc = fitz.open(path)
            for page_num, page in enumerate(doc):
                text = page.get_text().strip()
                if not text:
                    continue

                for chunk in self._chunk_text(text):
                    documents.append({
                        "text": chunk,
                        "source": path.name,
                        "page": page_num + 1
                    })

        return documents
