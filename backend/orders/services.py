
def calculate_order_price(items):
    """calculate order price for show current user total price buying products"""
    price_order_list = []
    quantity_order_list = []
    discount_order_list = []

    total_price = []

    for item in items:
        price_order_list.append(item.get('product').model.price)
        quantity_order_list.append(item.get('quantity'))
        try:
            discount_order_list.append(item.get('product').discount.value)
        except AttributeError:
            discount_order_list.append(None)

    for price, quantity, discount in zip(price_order_list, quantity_order_list, discount_order_list):
        if discount is not None:
            total_price.append((price - price * discount) * quantity)
        else:
            total_price.append(price * quantity)

    return sum(total_price)

