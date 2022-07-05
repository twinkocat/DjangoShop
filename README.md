# DjangoShop
_______________________
Users

register user
http://127.0.0.1:8000/api/v1/users/register/
_______________________
Products

show all products
http://127.0.0.1:8000/api/v1/products/

or show detail product from ID
http://127.0.0.1:8000/api/v1/products/<:id>/
_______________________
Orders

show orders for current user only
http://127.0.0.1:8000/api/v1/orders/my/

show detail order for current user from ID
http://127.0.0.1:8000/api/v1/orders/my/<:id>/

create order with current login user
http://127.0.0.1:8000/api/v1/orders/create/ 

for create order need authenticate and type json in Raw data: 
quantity product and product id

{
        "items": [
            {
                "quantity": 3,
                "product": 1
            },
            {
                "quantity": 3,
                "product": 2
            },
            {
                "quantity": 3,
                "product": 3
            },
        ],
}
