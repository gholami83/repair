from rest_framework.viewsets import ModelViewSet
from .models import Pair
from .api.serializers import MakePairSerializer


class MakePairViewSets(ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = MakePairSerializer