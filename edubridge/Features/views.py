from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import AnalyzeTextSerializer
from Features.nlp.keyword_model import KeywordExtractor
from Features.classification.cluster_classifier import ClusterClassifier

# Initialize once (important for performance)
keyword_extractor = KeywordExtractor()
cluster_classifier = ClusterClassifier()


class AnalyzeIssueAPIView(APIView):
    """
    Takes teacher classroom issue text
    → Extracts canonical issues
    → Classifies into NEP clusters (A/B/C)
    """

    def post(self, request):
        serializer = AnalyzeTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]

        # NLP → Keyword extraction
        issues = keyword_extractor.extract_keywords(text)

        # Classification
        cluster_result = cluster_classifier.classify(issues)

        return Response({
            "input_text": text,
            "detected_issues": issues,
            "cluster_result": cluster_result
        }, status=status.HTTP_200_OK)
