from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("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")
)

class GenAIModuleFormatter:
    def __init__(self, use_genai=True):
        self.use_genai = use_genai

    def format_module(self, text):
        if not self.use_genai:
            # Fallback formatter (NO API CALL)
            return {
                "title": "Microlearning Module (Offline)",
                "content": text[:500],  # safe truncation
                "source": "static-policy-content"
            }

        # 🔴 GenAI path (only when enabled)
        from openai import OpenAI
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert teacher trainer."},
                {"role": "user", "content": text}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content

