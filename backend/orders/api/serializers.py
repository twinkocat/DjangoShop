from rest_framework import serializers

from orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderSelfSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source='user.get_full_name')
    user_username = serializers.CharField(source='user.username')

    class Meta:
        model = Order
        fields = 'id', 'user_full_name', 'user_username', 'product', 'get_total_price'
        depth = 2
