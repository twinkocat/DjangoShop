from django.contrib import admin


def mark_discount(discount):
    def action(modeladmin, request, queryset):
        queryset.update(discount=discount)

    action.short_description = 'Применить: {0}'.format(discount.name)
    action.__name__ = '{0}'.format(discount.pk)

    return action


@admin.action(description='Удалить скидку')
def delete_discount(modeladmin, request, queryset):
    queryset.update(discount='')
    modeladmin.message_user(request, f'{queryset.count()} скидок было убранно с выбранных товаров')

