from django.shortcuts import render
from .models import Book, Customer, Order



def book_page(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def customer_page(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


def order_page(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


#manubasmi alohida books custmoerala/ ha shular 