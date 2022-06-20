from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Название')

    class Meta:
        verbose_name = 'Бренд продукта'
        verbose_name_plural = 'Бренды продуктов'

    def __str__(self):
        return self.name
