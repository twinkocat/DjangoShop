from django.db import models

from products.models.type import Type
from products.models.brand import Brand
from products.models.model import Model
from products.models.discounts import Discount
from products.services import get_discount, check_available


class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип продукта')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд продукта')
    model = models.OneToOneField(Model, on_delete=models.PROTECT, verbose_name='Модель продукта')
    available = models.BooleanField(default=False)
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT,
                                 verbose_name='Примененная скидка', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.type} | {self.brand} | {self.model}'

    def save(self, *args, **kwargs):
        check_available(self.model.count, self)

        super().save(*args, **kwargs)

    def get_discount(self):
        return get_discount(self.discount, self.model.price)
