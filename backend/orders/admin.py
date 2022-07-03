from django.contrib import admin
from django.contrib.admin import ModelAdmin

from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass