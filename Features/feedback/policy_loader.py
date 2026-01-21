import fitz  # PyMuPDF

class PolicyLoader:
    def __init__(self, pdf_paths: list):
        self.pdf_paths = pdf_paths

    def load_documents(self):
        documents = []

        for path in self.pdf_paths:
            doc = fitz.open(path)
            for page_num, page in enumerate(doc):
                text = page.get_text()
                if text.strip():
                    documents.append({
                        "text": text,
                        "source": path,
                        "page": page_num + 1
                    })

        return documents
