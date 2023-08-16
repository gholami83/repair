from rest_framework import serializers
from rest_framework.fields import empty
from ..models import Driver
from pair.models import Pair


class DriverSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get("view")
        if view.action in [
            "list",
            "retrieve",
        ] :
            self.fields["driver"] = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = [
            'driver',
            'pair_description',
        ]
    def get_driver(self, instance):
        return instance.driver.username

