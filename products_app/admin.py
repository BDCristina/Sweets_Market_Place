from django.contrib import admin

# Register your models here.
from products_app.models.product import Product
from products_app.models.category import Category
from products_app.models.manufacturer import Manufacturer


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)




