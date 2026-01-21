from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("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")
)

class PolicyRephraser:
    def simplify(self, policy_text: str):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You simplify official education policy text. "
                        "Do NOT add new information."
                    )
                },
                {"role": "user", "content": policy_text}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content
