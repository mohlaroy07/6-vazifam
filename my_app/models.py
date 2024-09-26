from django.db import models


class Book(models.Model):
    image = models.ImageField(upload_to="book-images/")

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.title} {self.author} {self.price} {self.published_date}"


class Customer(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.id} {self.full_name} {self.email} {self.phone_number}"


class Order(models.Model):
    order_date = models.DateField()
    count = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.order_date} {self.count} {self.price}"
