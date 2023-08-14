from rest_framework.viewsets import ModelViewSet
from .api.serializers import DriverSerializer
from .models import Driver


class DriverViewSets(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
