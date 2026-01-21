from Features.feedback.policy_loader import PolicyLoader
from Features.feedback.policy_retriever import PolicyRetriever
from Features.feedback.policy_feedback_generator import PolicyFeedbackGenerator


class FeedbackEngine:
    def __init__(self):
        self.policy_docs = PolicyLoader([
            "NEP_Final_English_0.pdf",
            "Guidelines50HoursCpd.pdf",
            "background_note_teacher_education.pdf"
        ]).load()

        self.retriever = PolicyRetriever(self.policy_docs)
        self.generator = PolicyFeedbackGenerator()

    def generate_feedback(self, issue_text, cluster):
        issue_keys = [i["key"] for i in cluster.get("issues", [])]
        policy_docs = self.retriever.retrieve(issue_keys)

        return self.generator.generate(
            issue_text,
            cluster["cluster_name"],
            policy_docs
        )
