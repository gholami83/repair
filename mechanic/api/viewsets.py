from rest_framework.viewsets import ModelViewSet 
from .serializers import MechanicSerializer
from ..models import Mechanic


class MechanicViewSet(ModelViewSet):
    serializer_class = MechanicSerializer
    queryset = Mechanic.objects.all()