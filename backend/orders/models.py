from django.db import models
from django.db.models import Avg

from orders.services import calculate_price
from products.models import Product

from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product)

    def get_total_price(self):
        return calculate_price(self.product)


