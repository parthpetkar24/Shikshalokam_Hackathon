from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import AnalyzeTextSerializer, MicroModuleRequestSerializer

from Features.nlp.keyword_model import KeywordExtractor
from Features.nlp.cluster_classifier import ClusterClassifier
from Features.feedback.feedback_engine import FeedbackEngine
from Features.microlearning.micro_module_selector import MicroModuleSelector

keyword_extractor = KeywordExtractor()
cluster_classifier = ClusterClassifier()
feedback_engine = FeedbackEngine()
micro_module_selector = MicroModuleSelector()


@method_decorator(csrf_exempt, name='dispatch')
class AnalyzeIssueAPIView(APIView):

    def post(self, request):
        serializer = AnalyzeTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = (
            serializer.validated_data.get("description")
            or serializer.validated_data.get("text")
        )

        try:
            issues = keyword_extractor.extract_keywords(text)

            if not issues:
                return Response({
                    "input_text": text,
                    "detected_issues": [],
                    "cluster": None,
                    "feedback": None,
                    "micro_module": None,
                    "message": "Please provide more detailed classroom input."
                }, status=status.HTTP_200_OK)
            cluster_result = cluster_classifier.identify_cluster(issues)
            feedback = feedback_engine.generate_feedback(
                nlp_output=issues,
                cluster_result=cluster_result,
                raw_issue=text
            )
            micro_module = micro_module_selector.select(cluster_result)

            return Response({
                "input_text": text,
                "detected_issues": issues,
                "cluster": cluster_result,
                "feedback": feedback,
                "micro_module": micro_module
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_exempt, name='dispatch')
class MicroModuleAPIView(APIView):
    def post(self, request):
        serializer = MicroModuleRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        topic = serializer.validated_data["topic"]

        try:
            module = micro_module_selector.select({
                "cluster_id": topic,
                "confidence": 1.0,
                "issues": []
            })
            return Response(module)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
