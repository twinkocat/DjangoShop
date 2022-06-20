from django.db import models
from django.conf import settings

from products.models import Product
from products.services import product_photo_path


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   verbose_name="Продукт", related_name='photos')
    photo = models.ImageField(max_length=256, upload_to=product_photo_path, verbose_name='Фото продукта')

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'

    def __str__(self):
        return f'{self.product_id} | {self.photo}'

    @property
    def image_url(self):
        return "{0}{1}".format('http://127.0.0.1:8000', self.photo.url)

