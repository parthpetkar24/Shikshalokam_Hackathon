from rest_framework import serializers


class AnalyzeTextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
