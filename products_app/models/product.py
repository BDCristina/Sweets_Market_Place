# products_app/models.py
from django.db import models
from .category import Category
from .manufacturer import Manufacturer


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    available_quantity = models.PositiveIntegerField(default=0)
    ingredients = models.TextField(null=True)
    weight_grams = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

