from babel.numbers import format_decimal
from decimal import Decimal


def format_price(price: Decimal) -> str:
    """Временно взята логика с
     https://github.com/tough-dev-school/education-backend/tree/master/src/products
                                                            спасибо :3
     """
    if price is not None and price:
        return format_decimal(price, locale='ru_RU')

    return '0'


def format_old_price(old_price: Decimal, new_price: Decimal) -> str:
    formatted_new_price = format_price(new_price)
    formatted_old_price = format_price(old_price)

    if formatted_old_price == '0':
        return f'{formatted_new_price} UAH'

    formatted_old_price = ''.join([f'{digit}\u0336' for digit in formatted_old_price])
    formatted_old_price = formatted_old_price.replace('\xa0\u0336', '')

    return f'{formatted_old_price} {formatted_new_price} UAH'


def get_discount(discount, price: Decimal) -> dict:
    """Расчет скидки и формат стоимости"""
    if discount is not None and discount:
        discount_price = price - (price * discount.value)
        return {
            'discount_name': discount.name,
            'discount_value': f'{discount.value * 100}%',
            'discount_price': f'{discount_price} UAH'
        }


def check_available(count, product):
    """Проверка на наличие на складе"""
    if count != 0:
        product.available = True
    else:
        product.available = False


def formatted_available(available) -> str:
    """Формат поля 'В наличии ' в зависимости от аргумента, не есть правильно для фроненда(Сашка)"""
    if available is True:
        return 'В наличии'
    if available is False:
        return 'Нет в наличии'


def product_photo_path(instance, filename):
    """Папка хранения фотографий продукта"""
    path = f'product_photos/{instance.product.brand}-{instance.product.model}/{filename}'
    return path.replace(' ', '-')
