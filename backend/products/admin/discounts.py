from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models.discounts import Discount


@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    pass
