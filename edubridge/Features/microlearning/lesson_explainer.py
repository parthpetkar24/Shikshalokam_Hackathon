class LessonExplainer:
    @staticmethod
    def explain(policy_intent: str, focus: str) -> dict:
        """
        Deterministic, human-readable explanation generator.
        NO hallucination, NO OCR noise.
        """

        explanation = (
            f"This policy focuses on {focus}. "
            f"In simple terms, {policy_intent.lower()}"
        )

        classroom_example = (
            f"For example, a teacher can apply this by making small changes "
            f"in daily classroom practice related to {focus}."
        )

        action_step = (
            f"Choose one simple activity this week that improves {focus} "
            f"and reflect on its impact on students."
        )

        reflection = (
            "What worked well for your students, and what would you improve next time?"
        )

        return {
            "explanation": explanation,
            "example": classroom_example,
            "action": action_step,
            "reflection": reflection
        }
