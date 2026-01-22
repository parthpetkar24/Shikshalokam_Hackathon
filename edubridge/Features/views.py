from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Features.nlp.keyword_model import KeywordExtractor
from Features.nlp.cluster_classifier import ClusterClassifier
from Features.feedback.feedback_engine import FeedbackEngine
from Features.microlearning.micro_module_selector import MicroModuleSelector
from Features.serializer import MicroModuleRequestSerializer

@api_view(["POST"])
def analyze_feedback(request):
    issue = request.data.get("issue")

    if not issue:
        return Response({"error": "Missing issue"}, status=400)

    extractor = KeywordExtractor()
    classifier = ClusterClassifier()
    engine = FeedbackEngine()

    issues = extractor.extract_keywords(issue)
    cluster = classifier.identify_cluster(issues)
    feedback = engine.generate_feedback(issue, cluster)

    return Response({
        "success": True,
        "issue": issue,
        "cluster": cluster["cluster_name"],
        "confidence": cluster["confidence"],
        "feedback": feedback
    })

@api_view(["POST"])
def generate_micro_module(request):
    serializer = MicroModuleRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    topic = serializer.validated_data["topic"]
    selector = MicroModuleSelector()

    module = selector.select(topic)

    return Response({
        "success": True,
        "micro_module": module
    }, status=200)
