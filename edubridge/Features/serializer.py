# Features/serializer.py

from rest_framework import serializers


class AnalyzeTextSerializer(serializers.Serializer):
    description = serializers.CharField(required=True, allow_blank=False)


class MicroModuleRequestSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True, allow_blank=False)
