from fastapi import FastAPI
from pydantic import BaseModel
from keyword_model import KeywordExtractor

app = FastAPI(title="Teacher Keyword Extraction API")

model = KeywordExtractor()

class InputText(BaseModel):
    text: str

@app.post("/extract-keywords")
def extract_keywords(data: InputText):
    keywords = model.extract_keywords(data.text)
    return {
        "input_text": data.text,
        "keywords": keywords
    }
