from google import genai
from django.conf import settings

class GeminiSummarizer:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def summarize(self, policy_text: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[
                    {
                        "role": "user",
                        "parts": [
                            {
                                "text": (
                                    "Summarize the following government policy text. "
                                    "Do not add advice or interpretation.\n\n"
                                    + policy_text
                                )
                            }
                        ]
                    }
                ]
            )
            return response.text.strip()

        except Exception:
            return (
                "This micro-learning module is derived from official policy documents.\n\n"
                + policy_text[:800]
                + "..."
            )
