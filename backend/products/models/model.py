from django.db import models

from products.services import format_price, format_old_price


class Model(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Модель")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name="Количество на складе")
    description = models.TextField(blank=False, verbose_name="Описание", default='description')

    class Meta:
        verbose_name = 'Модель продукта'
        verbose_name_plural = 'Модели продуктов'

    def __str__(self):
        return f'{self.name}'

    def get_price_display(self):
        return format_price(self.price)

    def get_old_price_display(self):
        return format_price(self.old_price)

    def get_formatted_price_display(self):
        return format_old_price(self.old_price, self.price)

