# Features/urls.py

from django.urls import path
from Features.views import analyze_feedback, generate_micro_module

urlpatterns = [
    path("analyze/", analyze_feedback, name="analyze-issue"),
    path("micro-module/", generate_micro_module, name="micro-module"),
]
