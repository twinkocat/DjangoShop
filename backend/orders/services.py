from django.db.models import Avg


def calculate_price(product):
    price = product.model.price
    return str(price)

