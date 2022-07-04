from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from orders.models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.get_or_create(order=order, **item_data)
        return order


class SelfOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSelfSerializer(serializers.ModelSerializer):
    items = SelfOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
