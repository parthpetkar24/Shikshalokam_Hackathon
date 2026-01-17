# microlearning/genai_module_formatter.py

class GenAIModuleFormatter:
    """
    Formats microlearning content.
    Works in TWO modes:
    1. Offline (NO GenAI, safe for testing & demo)
    2. Online (GenAI enabled later)
    """

    def __init__(self, use_genai=False):
        self.use_genai = use_genai

    def format_module(self, raw_text: str):
        """
        Returns a structured microlearning module
        """

        if not self.use_genai:
            # ✅ OFFLINE FALLBACK (NO API CALL)
            return {
                "title": "Microlearning Module (Offline Mode)",
                "learning_objectives": [
                    "Understand the classroom problem",
                    "Apply simple interventions",
                    "Reflect on teaching practice"
                ],
                "content": raw_text[:800],  # safe truncation
                "activity": "Reflect on how this applies to your classroom",
                "source": "NEP 2020 | DIET | Static Content"
            }

        # 🔴 GENAI MODE (future use only)
        from openai import OpenAI
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert teacher trainer."},
                {"role": "user", "content": raw_text}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content
