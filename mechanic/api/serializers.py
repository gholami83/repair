from rest_framework import serializers
from ..models import Mechanic


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = [
            'mechanic',
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['mechanic'] = instance.mechanic.username
        return representation
