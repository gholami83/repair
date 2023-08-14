from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Pair
from .api.serializers import MakePairSerializer, UpdatePairSerializer


class MakePairViewSets(ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = MakePairSerializer
    
class UpdatePair(ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = UpdatePairSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    