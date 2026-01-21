from Features.feedback.safe_gemini import SafeGemini


class PolicyFeedbackGenerator:
    def __init__(self):
        self.llm = SafeGemini()

    def generate(self, issue, cluster, policy_docs):
        policy_excerpt = policy_docs[0]["text"][:600] if policy_docs else ""

        prompt = f"""
Teacher Issue:
{issue}

Cluster:
{cluster}

Policy Context:
{policy_excerpt}

Write institutional, issue-specific feedback aligned with NEP 2020.
"""

        return self.llm.generate(prompt)
