from rest_framework import serializers
from ..models import TechnicalAssistant
from django.contrib.auth import get_user_model


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalAssistant
        fields = [
            'assistant'
        ]
                

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['assistant'] = instance.assistant.username
        return representation