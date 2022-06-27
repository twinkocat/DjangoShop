from rest_framework import serializers

from orders.models import Order


class OrderSelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
