# feedback/genai_rephraser.py
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

class PolicyRephraser:
    def generate_feedback(self, issue, cluster, policy_text):
        prompt = f"""
        You are an expert teacher mentor working with DIET faculty.

        Teacher issue:
        "{issue}"

        Cluster:
        {cluster}

        Relevant NEP / CPD policy excerpt:
        {policy_text}

        TASK:
        1. Explain why this issue occurs in classrooms
        2. Suggest two immediate classroom strategies
        3. Suggest one short micro-learning support
        4. Keep it practical and teacher-friendly
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content
