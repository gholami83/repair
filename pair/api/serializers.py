from rest_framework.serializers import ModelSerializer
from ..models import Pair


class MakePairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = [
            'pair_request',
            'date',
        ]   

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pair_request'] = instance.pair_request.pair_description00000000000000
        return representation
