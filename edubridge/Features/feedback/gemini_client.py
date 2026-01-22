from google import genai
from django.conf import settings

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY

        )

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=prompt
        )

        # ✅ SAFE TEXT EXTRACTION (handles all SDK variants)
        try:
            # New SDK format
            return response.candidates[0].content.parts[0].text.strip()
        except Exception:
            try:
                # Older SDK fallback
                return response.text.strip()
            except Exception as e:
                raise RuntimeError(f"Gemini response parse failed: {e}")
