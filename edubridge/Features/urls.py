from django.urls import path
from Features.views import AnalyzeIssueAPIView,MicroModuleAPIView

urlpatterns = [
    path("analyze/", AnalyzeIssueAPIView.as_view(), name="analyze-issue"),
    path("micro-module/", MicroModuleAPIView.as_view()),
]
