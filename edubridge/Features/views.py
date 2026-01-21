
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Features.serializer import AnalyzeTextSerializer
from Features.nlp.keyword_model import KeywordExtractor
from Features.nlp.cluster_classifier import ClusterClassifier
from Features.feedback.policy_loader import PolicyLoader
from Features.feedback.policy_retriever import PolicyRetriever
from Features.feedback.feedback_engine import FeedbackEngine
import os
from openai import OpenAI

# LOAD POLICY PDFs ONCE 
PDF_PATHS = [
    "data/NEP_Final_English_0.pdf",
    "data/Guidelines50HoursCpd.pdf",
    "data/background_note_teacher_education.pdf",
]

policy_documents = PolicyLoader(PDF_PATHS).load()


@api_view(["POST"])
def analyze_feedback(request):
    issue_text = request.data.get("issue", "")
    cluster = request.data.get("cluster", {})

    # ✅ Create GenAI client
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # ✅ Pass client to FeedbackEngine
    feedback_engine = FeedbackEngine(client)

    result = feedback_engine.generate_feedback(
        issue_text=issue_text,
        cluster=cluster
    )

    return Response(result)
