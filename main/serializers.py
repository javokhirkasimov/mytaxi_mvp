from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['driver', 'client']


class StatusUpdateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
