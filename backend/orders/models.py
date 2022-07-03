from django.db import models

from orders.services import calculate_order_price
from products.models import Product

from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return f'User:{self.user}|Total price:{self.total_price}'

    def save(self, *args, **kwargs):

        calculate_order_price(self.items)

        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
