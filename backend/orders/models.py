from django.db import models

from products.models import Product

from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return f'Order ID:{self.id} ||| User:{self.user}|Total price:{self.total_price}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Order ID:{self.order.id} ||| Customer:{self.order.user} ||| Product:{self.product}'
