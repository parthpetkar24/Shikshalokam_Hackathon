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

    def post(self, request):
        serializer = AnalyzeTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]

        try:
            issues = keyword_extractor.extract_keywords(text)

            if not issues:
                return Response({
                    "detected_issues": [],
                    "cluster_result": "Insufficient data",
                    "message": "Please provide more classroom details."
                }, status=status.HTTP_200_OK)

            cluster_result = cluster_classifier.classify(issues)

            return Response({
                "input_text": text,
                "detected_issues": issues,
                "cluster_result": cluster_result
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
