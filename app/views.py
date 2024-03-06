# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def product(request):
    return render(request, 'product.html')

def profile(request):
    return render(request, 'profile.html')

#email and username validation view
def check_username_avialability(request):
    username = request.GET.get('username', '')
    username_exist = User.objects.filter(username=username).exists()
    response = {
        'availabel': not username_exist
    }
    return JsonResponse(response)

def check_email_availability(request):
    email = request.GET.get ('email', '')
    email_exists = User.objects.filter(email=email).exists()
    response = {
        'available': not email_exists
    }
    return JsonResponse(response)

# -------signup user -----------

def signupuser(request):
    if request.method == 'POST':
        firstname = request.POST.get("first name")
        lastname = request.POST.get("last name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password") 
        user = User.objects.create_user(
            firstname=firstname,
            lastname=lastname, 
            username=username,
            email=email,
            password=password,
        )
        user.save()
        messages.success(request, 'Your account has been create successfully!')
        return redirect("/")
    return render(request, "signup.html")


#-------------login user view----------------
def loginuser(request):
    if request.user.is_authenticated:
        print(User.email)
        return redirect("/")
    else:
        print("User is not authenticated")
    
    if request.method == 'POST':
        Username = request.POST.get('Username')
        password = request.POST.get('password')
        print("user is not None")
        login(request,User)
        print(User.email,"logged in")
        return render(request,"index.html")
    else:
        print("User is None")
        return render(request, 'login.html')
# ------------logout user view-----------------
    
    @login_required(login_url='/login/')
    def logoutUser(request):
        logout(request)
        print("User logged out")

# ---print(User.is_authenticated)
        return redirect("/")



def shop(request):
    return render(request, 'shop.html')

def productdetails(request):
    return render(request, 'productdetails.html')

def buy(request):
    return render(request, 'buy.html')
