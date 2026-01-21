# Features/serializer.py

from rest_framework import serializers


class AnalyzeTextSerializer(serializers.Serializer):
    issue = serializers.CharField(required=True)



class MicroModuleRequestSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True, allow_blank=False)
