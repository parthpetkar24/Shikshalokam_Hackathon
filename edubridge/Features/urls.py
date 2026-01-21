# Features/urls.py

from django.urls import path
from Features.views import analyze_feedback

urlpatterns = [
    path("analyze/", analyze_feedback, name="analyze-issue"),
]
