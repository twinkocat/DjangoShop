from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=255, verbose_name='Навание')
    value = models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Размер скидки')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name
