from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
import os

from Features.nlp.keyword_model import KeywordExtractor
from Features.nlp.cluster_classifier import ClusterClassifier
from Features.feedback.feedback_engine import FeedbackEngine


@api_view(["POST"])
def analyze_feedback(request):
    # 1️⃣ Get raw issue text from frontend
    issue_text = request.data.get("issue", "").strip()

    if not issue_text:
        return Response({
            "error": "No issue text provided"
        }, status=400)

    # 2️⃣ Keyword extraction (MANDATORY)
    extractor = KeywordExtractor()
    canonical_issues = extractor.extract_keywords(issue_text)

    # 3️⃣ Cluster identification (MANDATORY)
    classifier = ClusterClassifier()
    cluster = classifier.identify_cluster(canonical_issues)

    # 4️⃣ Create OpenAI client (API key from .env)
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # 5️⃣ Generate policy-grounded feedback
    engine = FeedbackEngine(client)
    feedback_response = engine.generate_feedback(
        issue_text=issue_text,
        cluster=cluster
    )

    # 6️⃣ Final response to frontend
    return Response({
        "detected_issues": canonical_issues,
        "cluster": cluster,
        "feedback": feedback_response["feedback"]
    })
