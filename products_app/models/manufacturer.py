from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


Manufacturer._meta.app_label = 'products_app'

