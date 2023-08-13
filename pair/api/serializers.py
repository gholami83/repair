from rest_framework.serializers import ModelSerializer
from ..models import Pair


class PairSerializer(ModelSerializer):
    ModelSerializer.
    class Meta:
        model = Pair
        fields = [

        ]