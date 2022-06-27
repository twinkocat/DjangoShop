
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from config.current_user import get_current_user
from orders.api.serializers import OrderSelfSerializer
from orders.models import Order


class OrderSelfView(ListAPIView):
    serializer_class = OrderSelfSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_current_user()
        return Order.objects.filter(user=user)
