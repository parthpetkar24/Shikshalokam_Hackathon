import openai
import os

openai.api_key = os.getenv("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")

class PolicyRephraser:
    def simplify(self, policy_text: str):
        prompt = f"""
Rephrase the following official policy text into
simple, teacher-friendly language.
DO NOT add new information.

TEXT:
{policy_text}
"""

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You simplify official education policy text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response["choices"][0]["message"]["content"]
