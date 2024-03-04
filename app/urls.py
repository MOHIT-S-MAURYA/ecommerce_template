from django.contrib import admin
from django.urls import include, path
from app import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]