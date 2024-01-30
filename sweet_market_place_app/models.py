from django.db import models
from django.conf import settings
from products_app.models.product import Product


# Create your models here.
class Mesaj(models.Model):
    STATUS_CHOICES = [
        ('necitit', 'Necitit'),
        ('rezolvat', 'Rezolvat'),
    ]

    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    mesaj = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='necitit')
    data_inregistrare = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
