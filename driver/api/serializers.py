from rest_framework.serializers import ModelSerializer
from ..models import Driver
from pair.models import Pair


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver',
            'pair_description',
        ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['driver'] = instance.driver.username
        return representation

