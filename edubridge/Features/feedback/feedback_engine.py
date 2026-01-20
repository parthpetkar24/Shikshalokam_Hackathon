from Features.feedback.policy_loader import PolicyLoader
from Features.feedback.policy_retriever import PolicyRetriever
from Features.feedback.genai_rephraser import PolicyRephraser
from django.conf import settings

PDF_PATHS = [
    settings.DATA_DIR / "NEP_Final_English_0.pdf",
    settings.DATA_DIR / "Guidelines50HoursCpd.pdf",
    settings.DATA_DIR / "background_note_teacher_education.pdf",
    settings.DATA_DIR / "EmpoweringEducatorsTeacherTrainingandProfessionalDevelopmentinNEP2020India_e1xn0wSl.pdf",
]


class FeedbackEngine:
    def __init__(self):
        loader = PolicyLoader(PDF_PATHS)
        documents = loader.load_documents()
        self.retriever = PolicyRetriever(documents)
        self.rephraser = PolicyRephraser()

    def generate_feedback(self, nlp_output: list, cluster_result: dict, raw_issue: str):
        """
        nlp_output: Fix 1 output
        cluster_result: Fix 2 ClusterClassifier output
        raw_issue: original user text
        """

        if not nlp_output or cluster_result["cluster_id"] == "Insufficient data":
            return {
                "error": "Issue not identified clearly"
            }

        issue_keys = [item["key"] for item in nlp_output]

        policy_snippets = self.retriever.retrieve(issue_keys)

        feedback_items = []

        for item in policy_snippets:
            feedback = self.rephraser.generate_feedback(
                issue=raw_issue,
                cluster=cluster_result["cluster_name"],
                policy_text=item["text"]
            )

            feedback_items.append({
                "feedback": feedback,
                "source_pdf": item["source"],
                "page": item["page"]
            })

        return {
            "cluster": cluster_result["cluster_name"],
            "confidence": cluster_result["confidence"],
            "issues": issue_keys,
            "feedback": feedback_items
        }
