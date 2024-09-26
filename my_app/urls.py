from django.urls import path
from .views import book_page, customer_page, order_page

urlpatterns = [
    path('', book_page, name='book_page'),
    path('customers/', customer_page, name='customer_page'),
    path('orders/', order_page, name='order_page'),
]
