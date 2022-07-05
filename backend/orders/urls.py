from django.urls import path

from orders.api.view import OrderSelfView, OrderCreateView, OrderDetailView

urlpatterns = [
    path('my/', OrderSelfView.as_view()),
    path('my/<pk>/', OrderDetailView.as_view()),
    path('create/', OrderCreateView.as_view()),

]
