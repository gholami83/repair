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
    def get_driver(self, instance):
        return instance.driver.username

