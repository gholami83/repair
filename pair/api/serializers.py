from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Pair
from driver.models import Driver


class PairRequestSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields =[
            'driver',
            'pair_description',
        ]

class MakePairSerializer(ModelSerializer):
    pair_request = PairRequestSerializer()
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
        ]   
        
    # def get_pair_request(self, instance):
    #     return instance.pair_request.pair_description

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
    def get_pair_request(self, instance):
        return instance.pair_request.pair_description

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
