# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, CarouselImage


# Create your views here.

def index(request):
    products = Product.objects.all()
    carousel_images = CarouselImage.objects.all()
    return render(request, 'index.html', {'products': products, 'carousel_images': carousel_images})

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def product(request):
    return render(request, 'product.html')

def profile(request):
    return render(request, 'profile.html')

def productdetails(request):
    return render(request, 'productdetails.html')




# -------signup user -----------

def signupuser(request):
    if request.method == 'POST':
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password") 

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect("signup")
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, 'Your account has been create successfully!')
        return redirect("/")
    return render(request, "signup.html")


#-------------login user view----------------
def loginUser(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully!') 
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect("login")
    return render(request, "login.html")

# ------------logout user view-----------------
    
@login_required(login_url='/login/')
def logoutUser(request):
        logout(request)
        messages.success(request, 'You have been logged out successfully!')

# ---print(User.is_authenticated)
        return redirect("/")


# ------------shop view-----------------
def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def productdetails(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'productdetails.html', {'product': product})

def buy(request):
    return render(request, 'buy.html')
