from rest_framework import serializers

class AnalyzeTextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, allow_blank=False)

class MicroModuleRequestSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True, allow_blank=False)
