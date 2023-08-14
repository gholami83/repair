from rest_framework.serializers import ModelSerializer
from ..models import Pair


class MakePairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
        ]   
        
    def create(self, validated_data):
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pair_request'] = instance.pair_request.pair_description
        return representation

class UpdatePairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
            'asisstant_confirm',
        ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pair_request'] = instance.pair_request.pair_description
        return representation