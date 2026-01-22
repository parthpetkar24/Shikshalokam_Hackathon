
from rest_framework import serializers
from Features.microlearning.micro_module_config import MICRO_MODULE_POLICY_MAP

class AnalyzeTextSerializer(serializers.Serializer):
    issue = serializers.CharField(required=True)

class MicroModuleRequestSerializer(serializers.Serializer):
    topic = serializers.ChoiceField(
        choices=list(MICRO_MODULE_POLICY_MAP.keys())
    )