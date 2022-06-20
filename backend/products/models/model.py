from django.db import models

from products.services import format_price


class Model(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Модель")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    count = models.PositiveIntegerField(verbose_name="Количество на складе")
    description = models.TextField(blank=False, verbose_name="Описание", default='description')

    class Meta:
        verbose_name = 'Модель продукта'
        verbose_name_plural = 'Модели продуктов'

    def __str__(self):
        return f'{self.name}'

    def get_price_display(self):
        return format_price(self.price)


