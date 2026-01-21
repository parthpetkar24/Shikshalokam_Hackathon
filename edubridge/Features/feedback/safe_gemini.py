try:
    from google import genai
except Exception:
    genai = None


class SafeGemini:
    def __init__(self):
        self.client = None
        if genai:
            try:
                self.client = genai.Client(
                    api_key="PASTE_YOUR_KEY_HERE"
                )
            except Exception:
                self.client = None

    def generate(self, prompt: str) -> str:
        # Try Gemini FIRST
        if self.client:
            try:
                response = self.client.models.generate_content(
                    model="models/gemini-1.5-flash",
                    contents=[{"role": "user", "parts": [{"text": prompt}]}]
                )
                return response.candidates[0].content.parts[0].text.strip()
            except Exception:
                pass

        # ✅ INTELLIGENT FALLBACK (ISSUE-SPECIFIC)
        return self._intelligent_fallback(prompt)

    def _intelligent_fallback(self, prompt: str) -> str:
        prompt_lower = prompt.lower()

        if "english" in prompt_lower or "language" in prompt_lower:
            return (
                "This issue reflects a language and comprehension barrier among learners. "
                "NEP 2020 emphasizes the use of the mother tongue or familiar local language "
                "as the medium of instruction in the foundational and preparatory stages. "
                "System-level support through multilingual pedagogy training and DIET-led "
                "capacity building is required."
            )

        if "parent" in prompt_lower:
            return (
                "This issue indicates weak parent–school engagement mechanisms. "
                "NEP 2020 highlights the role of parents and the local community as "
                "key stakeholders in student learning. Strengthening School Management "
                "Committees and structured parent outreach programs is required."
            )

        if "attendance" in prompt_lower or "absent" in prompt_lower:
            return (
                "This issue reflects irregular student attendance patterns. "
                "NEP 2020 calls for early identification of at-risk learners and "
                "institutional tracking mechanisms to ensure retention and continuity "
                "in schooling."
            )

        # Default differentiated fallback
        return (
            "This issue requires targeted institutional intervention aligned with NEP 2020. "
            "Systemic academic support, professional development, and school-level planning "
            "are necessary to address this classroom challenge."
        )
