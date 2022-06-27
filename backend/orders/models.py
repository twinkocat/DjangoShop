from django.db import models

from products.models import Product

from users.models import User


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product)


