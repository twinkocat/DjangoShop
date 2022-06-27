from django.contrib import admin

from products.admin.model import ModelAdmin
from users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    ordering = ['username']
    list_display = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', ]
