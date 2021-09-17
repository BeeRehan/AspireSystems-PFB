from rest_framework import serializers
from .models import AppoinmentDetails


class AppoimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppoinmentDetails
        fields = "__all__"
