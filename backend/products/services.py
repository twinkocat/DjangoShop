from babel.numbers import format_decimal
from decimal import Decimal

"""in future i want to realize a changeble value for current user"""


def format_price(price: Decimal) -> str:
    """Formated price UAH current"""
    if price is not None and price:
        return f'{price} UAH'


def get_discount(discount, price: Decimal) -> dict:
    """Calculate discount price"""
    if discount is not None and discount:
        discount_price = price - (price * discount.value)
        return {
            'discount_name': discount.name,
            'discount_value': f'{discount.value * 100} %',
            'discount_price': f'{discount_price} UAH'
        }


def check_available(count, product):
    """Check available in stock"""
    if count != 0:
        product.available = True
    else:
        product.available = False


def formatted_available(available) -> str:
    """Not used on this moment"""
    if available is True:
        return 'В наличии'
    if available is False:
        return 'Нет в наличии'


def product_photo_path(instance, filename):
    """make a folder for photo model products"""
    path = f'product_photos/{instance.product.brand}-{instance.product.model}/{filename}'
    return path.replace(' ', '-')
