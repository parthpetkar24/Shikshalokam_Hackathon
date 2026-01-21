# microlearning/module_formatter.py

class MicroModuleFormatter:
    @staticmethod
    def format(summary: str) -> dict:
        return {
            "Module Title": "NEP 2020 Teacher Micro-Learning Module",
            "Learning Objective": (
                "Understand key NEP 2020 guidelines and apply them in classroom practice"
            ),
            "Key Concept": summary,
            "Activity 1 (5 min)": (
                "Identify one challenge from your classroom related to this concept"
            ),
            "Activity 2 (5 min)": (
                "Apply one suggested strategy in your next class"
            ),
            "Reflection Question": (
                "What change did you observe after applying this strategy?"
            ),
            "Time Breakdown": "10–15 Minutes",
            "Source": "Official NEP 2020 / NCERT / CPD Policy Documents"
        }
