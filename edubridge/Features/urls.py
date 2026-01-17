from django.urls import path
from Features.views import AnalyzeIssueAPIView

urlpatterns = [
    path("analyze/", AnalyzeIssueAPIView.as_view(), name="analyze-issue"),
]
