from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.admin.actions.product_action import mark_discount, delete_discount

from products.models.discounts import Discount
from products.models.product import Product


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'type', 'brand', 'model', 'available', 'discount',)
    readonly_fields = ('available',)
    list_filter = ('type', 'brand')
    ordering = ['type', ]
    actions = [delete_discount]

    def get_actions(self, request):
        actions = super(ProductAdmin, self).get_actions(request)

        for discount in Discount.objects.all():
            action = mark_discount(discount)
            actions[action.__name__] = (action,
                                        action.__name__,
                                        action.short_description)

        return actions

    # dict(mark_discount(discount) for discount in Discount.objects.all())



