from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .models import Pair
from .api.serializers import MakePairSerializer, UpdatePairSerializer,CostPairSerializer,PayPairSerializer


class MakePairViewSets(ModelViewSet):
    throttle_classes = [
        UserRateThrottle,
        AnonRateThrottle,
    ]
    def get_queryset(self):
        return Pair.objects.all()

    def get_permissions(self):
        if self.action == 'update':
            return [IsAuthenticated()]
        else :
            return []
        
    def get_serializer_class(self):
        if self.action == 'create':
            return MakePairSerializer
        else:
            return UpdatePairSerializer

class CostPairViewSets(ModelViewSet):
    queryset = Pair.objects.filter(assistant_confirm = True)
    serializer_class = CostPairSerializer
    permission_classes = [
        IsAuthenticated,
    ]

class PayPairViewSets(ModelViewSet):
    queryset = Pair.objects.filter(assistant_confirm = True,cost__isnull = False)
    serializer_class = PayPairSerializer
    permission_classes = [
        IsAuthenticated,
    ]