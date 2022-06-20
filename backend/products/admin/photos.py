from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models.photos import Photo


@admin.register(Photo)
class ProductPhotoAdmin(ModelAdmin):
    pass
