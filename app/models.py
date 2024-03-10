# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/products', null=True, blank=True)


    def __str__(self):
        return self.name

class CarouselImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images/carousel')