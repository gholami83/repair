from rest_framework import serializers
from ..models import TechnicalAssistant
from django.contrib.auth import get_user_model


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalAssistant
        fields = [
            'assistant'
        ]
    def get_assistant(self, instance):
        return instance.assistant.username
