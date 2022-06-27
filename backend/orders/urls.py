from django.urls import path

from orders.api.view import OrderSelfView

urlpatterns = [
    path('my/', OrderSelfView.as_view())

]