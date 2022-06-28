from django.db.models import Avg


def calculate_price(product):
    """calculate order price for show current user total price buying products"""
    price_value = product.values_list('model__price', flat=True)
    discount_value = product.values_list('discount__value', flat=True)

    total_price = []
    for price, discount in zip(price_value, discount_value):
        if discount is not None:
            total_price.append(price - price * discount)
        if discount is None:
            total_price.append(price)

    return sum(total_price)





