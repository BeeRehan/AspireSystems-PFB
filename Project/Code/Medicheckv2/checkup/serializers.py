from rest_framework import serializers
from .models import CheckupDetails

class CheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckupDetails
        fields = '__all__'