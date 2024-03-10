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
    path('login/', views.loginUser, name='login'),
    path("logout/", views.logoutUser, name="logout"),
    path('signup/', views.signupuser, name='signup'),
    path('shop/', views.shop, name='shop'),
    path('productdetails/', views.productdetails, name='productdetails'),
    ]