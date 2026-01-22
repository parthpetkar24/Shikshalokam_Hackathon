from Features.microlearning.lesson_explainer import LessonExplainer

class ModuleGenerator:
    def __init__(self, title, policy_intent, focus, pdf_name):
        self.title = title
        self.policy_intent = policy_intent
        self.focus = focus
        self.pdf_name = pdf_name

    def generate(self) -> dict:
        explained = LessonExplainer.explain(
            self.policy_intent,
            self.focus
        )

        return {
            "module_title": self.title,
            "policy_source": self.pdf_name,
            "policy_intent": self.policy_intent,
            "learning_objectives": [
                f"Understand the purpose of {self.title}",
                "Connect policy ideas to classroom practice",
                "Apply one practical teaching strategy",
                "Reflect on professional growth"
            ],
            "module_content": [
                {
                    "title": "What Does This Policy Mean?",
                    "points": [explained["explanation"]]
                },
                {
                    "title": "Why This Matters in Classrooms",
                    "points": [
                        "Supports better teaching practices",
                        "Improves student learning experience",
                        "Aligns with national education policy"
                    ]
                },
                {
                    "title": "Classroom Example",
                    "points": [explained["example"]]
                },
                {
                    "title": "Action You Can Try This Week",
                    "points": [explained["action"]]
                },
                {
                    "title": "Reflection Prompt",
                    "points": [explained["reflection"]]
                }
            ],
            "duration": "10–15 minutes"
        }
