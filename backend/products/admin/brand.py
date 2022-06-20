from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models.brand import Brand


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    pass
