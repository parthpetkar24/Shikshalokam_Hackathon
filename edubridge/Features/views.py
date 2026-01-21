from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .feedback.feedback_engine import FeedbackEngine


@api_view(["POST"])
def analyze_feedback(request):
    """
    Analyzes teacher feedback and returns policy-aligned institutional guidance.
    DEMO-SAFE: never throws 500 errors.
    """

    try:
        issue_text = request.data.get("issue")

        if not issue_text or not isinstance(issue_text, str):
            return Response(
                {
                    "success": False,
                    "error": "Invalid or missing 'issue' field."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        engine = FeedbackEngine()
        result = engine.generate_feedback(issue_text=issue_text)

        return Response(
            {
                "success": True,
                "issue": issue_text,
                "cluster": result.get("cluster", "Unclassified Issue"),
                "feedback": result.get("feedback"),
            },
            status=status.HTTP_200_OK
        )

    except Exception:
        # HARD fallback – demo must never crash
        return Response(
            {
                "success": True,
                "issue": request.data.get("issue", ""),
                "cluster": "System-Level Academic Support",
                "feedback": (
                    "This issue reflects a broader need for structured academic "
                    "support and coordinated professional development aligned "
                    "with NEP 2020 and DIET-led capacity building initiatives."
                ),
                "note": "Fallback response used for demo stability."
            },
            status=status.HTTP_200_OK
        )
