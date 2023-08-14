from rest_framework.serializers import ModelSerializer
from ..models import Pair


class MakePairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
        ]   
        
    def get_pair_request(self, instance):
        return instance.pair_request.pair_description

class UpdatePairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
            'asisstant_confirm',
        ]
    def get_pair_request(self, instance):
        return instance.pair_request.pair_description

class CostPairSerializer(ModelSerializer):
    class Meta:
        model = Pair 
        fields = [
            'pair_request',
            'date',
            'cost',
        ]

class PayPairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
            'cost',
            'payed',
        ]
    def get_pair_request(self, instance):
        return instance.pair_request.pair_description
