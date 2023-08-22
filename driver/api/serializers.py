from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import empty
from ..models import Driver
from pair.models import Pair


class DriverSerializer(serializers.ModelSerializer):
    driver = serializers.SerializerMethodField()
    class Meta:
        model = Driver
        fields = [
            'driver',
            'pair_description',
        ]
    def get_driver(self,instance):
        return {
            "username":instance.driver.username,
            "email":instance.driver.email,
        }