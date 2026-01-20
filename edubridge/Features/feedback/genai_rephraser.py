# feedback/genai_rephraser.py
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    project=os.getenv("OPENAI_PROJECT_ID")  # 🔑 REQUIRED
)

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
