import django_filters.rest_framework
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from ..models import Pair
from .serializers import MakePairSerializer, UpdatePairSerializer,CostPairSerializer,PayPairSerializer


class MakePairViewSets(ModelViewSet):
    queryset = Pair.objects.all()
    filterset_fields  = ['date','assistant_confirm']
    search_fields = ['date']
    ordering_fields= ["date"]
    throttle_classes = [    
        UserRateThrottle,
        AnonRateThrottle,
    ]
    # def get_queryset(self):
    #     queryset = Pair.objects.all()
    #     assistant_confirm = self.request.query_params.get('assistant_confirm')
    #     date = self.request.query_params.get('date')
    #     pair_request = self.request.query_params.get('pair_request')
    #     if assistant_confirm and date is not None:
    #         queryset = queryset.filter(assistant_confirm = assistant_confirm,date = date, pair_request_username = pair_request)
    #     return queryset
    
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