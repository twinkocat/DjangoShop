from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'

    def __str__(self):
        return self.name
