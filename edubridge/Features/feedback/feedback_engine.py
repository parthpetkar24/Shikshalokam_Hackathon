from feedback.policy_loader import PolicyLoader
from feedback.policy_retriever import PolicyRetriever
from feedback.genai_rephraser import PolicyRephraser
from django.conf import settings

PDF_PATHS = [
    settings.DATA_DIR / "NEP_Final_English_0.pdf",
    settings.DATA_DIR / "Guidelines50HoursCpd.pdf",
    settings.DATA_DIR / "background_note_teacher_education.pdf",
    settings.DATA_DIR / "EmpoweringEducatorsTeacherTrainingandProfessionalDevelopmentinNEP2020India_e1xn0wSl.pdf",
]


class FeedbackEngine:
    def __init__(self, use_genai=True):
        loader = PolicyLoader(PDF_PATHS)
        self.documents = loader.load_documents()
        self.retriever = PolicyRetriever(self.documents)
        self.rephraser = PolicyRephraser() if use_genai else None

    def generate_feedback(self, cluster: str):
        policy_snippets = self.retriever.retrieve(cluster)

        feedback = []

        for item in policy_snippets:
            text = item["text"]

            if self.rephraser:
                text = self.rephraser.simplify(text)

            feedback.append({
                "feedback": text,
                "source_pdf": item["source"],
                "page": item["page"]
            })

        return feedback
