from rest_framework import serializers
from ..models import Mechanic


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = [
            'mechanic',
        ]
        
    def get_mechanic(self,instance):
        return instance.mechanic.username
