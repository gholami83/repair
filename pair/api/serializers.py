from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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
    
    pair_request = serializers.SerializerMethodField()

    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
            'assistant_confirm',
        ]
    
    def get_pair_request(self, instance):
        return instance.pair_request.pair_description

class CostPairSerializer(ModelSerializer):
    pair_request = serializers.SerializerMethodField()
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
