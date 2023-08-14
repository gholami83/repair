from rest_framework.viewsets import ModelViewSet
from .serializers import AssistantSerializer
from ..models import TechnicalAssistant


class AssistantViewSet(ModelViewSet):
    serializer_class = AssistantSerializer
    queryset = TechnicalAssistant.objects.all()
