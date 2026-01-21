# Features/feedback/policy_feedback_generator.py
from Features.feedback.gemini_client import GeminiClient
class PolicyFeedbackGenerator:
    """
    Generates professional, institutional feedback
    aligned with NEP 2020 and CPD intent.

    This generator NEVER fails silently and NEVER
    returns generic fallback text.
    """

    def __init__(self, client):
        self.client = GeminiClient()

    def generate(self, issue: str, cluster: str, policy_docs: list):
        """
        Args:
            issue (str): Teacher-reported classroom issue
            cluster (str): Identified issue cluster
            policy_docs (list): Policy documents (may be empty or weak)

        Returns:
            str: Professional feedback text
        """

        # 🔹 Build policy context (if available)
        policy_context = ""

        if policy_docs:
            policy_context = "\n\n".join(
                f"Source: {doc.get('source', 'Policy Document')}\n"
                f"{doc.get('text', '')[:1200]}"
                for doc in policy_docs
            )

        # 🔹 Strong institutional prompt (policy-first)
        prompt = f"""
You are a senior academic expert working with SCERT and DIET institutions.

Teacher-reported classroom issue:
"{issue}"

Identified issue cluster:
"{cluster}"

Relevant education policy context (NEP 2020 and CPD guidelines):
{policy_context if policy_context else "Use your knowledge of NEP 2020 and CPD frameworks."}

Task:
Write professional, institutional feedback that:
1. Diagnoses the issue systemically (not as an individual teacher fault)
2. Aligns the issue with NEP 2020 intent and CPD mandates
3. Explains why the issue persists at classroom and institutional level
4. Prescribes actions at BOTH teacher and DIET / system level
5. Uses formal, authoritative policy language (not advisory tone)

Do NOT say that policy context is insufficient.
Do NOT provide generic advice.
Do NOT mention missing data.
"""

        return self.client.generate(prompt)
