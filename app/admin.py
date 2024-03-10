# admin.py
from django.contrib import admin
from .models import Product, CarouselImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'image', 'description') 

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image') 
