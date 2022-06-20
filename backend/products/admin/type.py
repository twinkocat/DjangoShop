from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models.type import Type


@admin.register(Type)
class TypeAdmin(ModelAdmin):
    pass