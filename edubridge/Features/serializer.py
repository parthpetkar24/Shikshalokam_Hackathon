from rest_framework import serializers

class AnalyzeTextSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)
    text = serializers.CharField(required=False)

    def validate(self, data):
        if not data.get("description") and not data.get("text"):
            raise serializers.ValidationError(
                "Either 'description' or 'text' is required."
            )
        return data


class MicroModuleRequestSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True, allow_blank=False)
