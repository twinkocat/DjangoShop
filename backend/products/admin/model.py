from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models.model import Model


@admin.register(Model)
class ModelAdmin(ModelAdmin):
    ordering = ['name']
