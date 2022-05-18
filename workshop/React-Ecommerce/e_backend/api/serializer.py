from rest_framework import serializers
from .models import Products
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class SiginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    client_id = serializers.CharField()
    client_secret = serializers.CharField()
    