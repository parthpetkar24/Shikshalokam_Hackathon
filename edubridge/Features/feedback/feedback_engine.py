from Features.feedback.policy_loader import PolicyLoader
from Features.feedback.policy_retriever import PolicyRetriever
from Features.feedback.policy_feedback_generator import PolicyFeedbackGenerator


class FeedbackEngine:
    """
    Generates professional, policy-grounded feedback aligned with
    NEP 2020 and CPD guidelines.
    """

    def __init__(self, client):
        """
        client: OpenAI / GenAI client
        """
        self.client = client

        # STEP 3.2 FIX — Load policies ONCE
        self.policy_loader = PolicyLoader([
            "NEP_Final_English_0.pdf",
            "Guidelines50HoursCpd.pdf",
            "background_note_teacher_education.pdf"
        ])

        self.policy_documents = self.policy_loader.load()
        self.policy_retriever = PolicyRetriever(self.policy_documents)

        # Professional feedback generator (NO rephrasing)
        self.policy_feedback_generator = PolicyFeedbackGenerator(self.client)

    def generate_feedback(self, issue_text: str, cluster: dict) -> dict:

        # FIX: Map cluster output → canonical issue key
        issue_keys = []

        if isinstance(cluster, dict):
            # Case 1: NLP cluster output
            if "issues" in cluster and cluster["issues"]:
                issue_keys = [item["key"] for item in cluster["issues"]]

            # Case 2: Fallback (cluster id only)
            elif "cluster_id" in cluster:
                if cluster["cluster_id"] == "A":
                    issue_keys = ["student_absenteeism"]


        # Retrieve relevant policy documents
        policy_docs = self.policy_retriever.retrieve(issue_keys)

        # HARD FALLBACK — No policy match
        if not policy_docs:
            return {
                "feedback": [
                    {
                        "feedback": (
                            "The reported issue reflects a need for strengthened "
                            "need-based professional development mechanisms as "
                            "outlined under the National Education Policy (NEP) 2020. "
                            "Institutional review and contextualized training support "
                            "are required."
                        )
                    }
                ]
            }

        # Generate PROFESSIONAL policy-grounded feedback
        feedback_text = self.policy_feedback_generator.generate(
            issue=issue_text,
            cluster=cluster.get("cluster_name", "Unclassified Issue"),
            policy_docs=policy_docs
        )

        # Final frontend-safe response
        return {
            "feedback": [
                {
                    "feedback": feedback_text
                }
            ]
        }
