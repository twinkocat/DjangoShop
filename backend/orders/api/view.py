
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from config.current_user import get_current_user
from orders.api.serializers import OrderSelfSerializer, OrderCreateSerializer
from orders.models import Order
from orders.services import calculate_order_price


class OrderSelfView(ListAPIView):
    serializer_class = OrderSelfSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_current_user()
        return Order.objects.\
            select_related('user'). \
            prefetch_related('items'). \
            filter(user=user)   # or self.request.user


class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSelfSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_current_user()
        return Order.objects. \
            select_related('user'). \
            prefetch_related('items'). \
            filter(user=user)  # or self.request.user


class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        return Order.objects.\
            select_related('user')

    def perform_create(self, serializer):

        total_price = calculate_order_price(serializer.validated_data['items'])
        user = get_current_user()

        serializer.save(user=user, total_price=total_price)  # or self.request.user
