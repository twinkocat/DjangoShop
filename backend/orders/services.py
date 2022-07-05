
def calculate_order_price(items):
    """calculate order price for show current user total price buying products"""

    total_price = []

    for item in items:
        price = item.get('product').model.price
        quantity = item.get('quantity')
        try:
            discount = item.get('product').discount.value
            total_price.append((price - price * discount) * quantity)
        except AttributeError:
            # method get apply this exception because getting NonType(haven`t field discount in data)
            total_price.append(price * quantity)

    return sum(total_price)


