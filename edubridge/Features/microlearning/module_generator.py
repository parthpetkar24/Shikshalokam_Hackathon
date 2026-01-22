from Features.microlearning.pdf_loader import PDFLoader
from Features.microlearning.text_cleaner import TextCleaner

class ModuleGenerator:
    def __init__(self, pdf_path, policy_intent=""):
        self.pdf_path = pdf_path
        self.policy_intent = policy_intent

    def generate(self) -> dict:
        raw = PDFLoader.load_pdf_text(self.pdf_path, skip_pages=3)
        text = TextCleaner.clean(raw)

        sections = self._extract_cpd_sections(text)
        module_content = self._build_module(sections)

        return {
            "module_title": "CPD Micro-Learning Module",
            "policy_source": self.pdf_path.name,
            "policy_intent": self.policy_intent,
            "learning_objectives": [
                "Understand the 50-hour CPD mandate",
                "Identify acceptable CPD activity types",
                "Plan CPD aligned with school needs",
                "Reflect on professional growth"
            ],
            "module_content": module_content,
            "duration": "10–15 minutes"
        }

    # ---------- CPD STRUCTURE EXTRACTION ----------

    def _extract_cpd_sections(self, text: str) -> dict:
        sections = {
            "overview": [],
            "types": [],
            "planning": [],
            "reflection": []
        }

        for sentence in text.split("."):
            sentence = sentence.strip()
            if len(sentence) < 120:
                continue

            s = sentence.lower()

            if "50 hour" in s or "continuous professional development" in s:
                sections["overview"].append(sentence)

            elif any(x in s for x in ["self-directed", "peer", "workshop", "course"]):
                sections["types"].append(sentence)

            elif any(x in s for x in ["plan", "annual", "school", "institution"]):
                sections["planning"].append(sentence)

            elif any(x in s for x in ["reflection", "evaluation", "monitoring"]):
                sections["reflection"].append(sentence)

        return sections

    # ---------- BUILD LEARNING MODULE ----------

    def _build_module(self, sections: dict) -> list:
        module = []

        if sections["overview"]:
            module.append({
                "title": "1. Understanding the 50-Hour CPD Requirement",
                "points": sections["overview"][:4]
            })

        if sections["types"]:
            module.append({
                "title": "2. Types of CPD Activities",
                "points": sections["types"][:5]
            })

        if sections["planning"]:
            module.append({
                "title": "3. Planning Your CPD",
                "points": sections["planning"][:4]
            })

        if sections["reflection"]:
            module.append({
                "title": "4. Reflection and Continuous Improvement",
                "points": sections["reflection"][:4]
            })

        return module
