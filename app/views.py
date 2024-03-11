from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Product, CarouselImage


# Create your views here.

# ------------index view-----------------
def index(request):
    products = Product.objects.all()
    carousel_images = CarouselImage.objects.all()
    return render(request, 'index.html', {'products': products, 'carousel_images': carousel_images})

# ------------contact view-----------------
def contact(request):
    return render(request, 'contact.html')

# ------------cart view-----------------
@login_required(login_url='/login/')
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_total = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

# ------------product view-----------------
def product(request):
    return render(request, 'product.html')

# ------------profile view-----------------
def profile(request):
    return render(request, 'profile.html')

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

# ------------productdetails view-----------------
def productdetails(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'productdetails.html', {'product': product})

# ------------buy view-----------------
def buy(request):
    return render(request, 'buy.html')

# ------------add to cart view-----------------
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        # User is authenticated, proceed with adding to cart
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        # Your additional logic here
        messages.success(request, f'{product.name} added to your cart.')
    else:
        # User is not authenticated, redirect to login page
        messages.info(request, 'Please log in to add items to your cart.')
        return redirect('login')

    return redirect('cart')

# ------------remove from cart view-----------------
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    # Delete the item from the cart
    cart_item.delete()

    messages.success(request, f'{cart_item.product.name} removed from your cart.')
    return redirect('cart')  # Change 'cart' to your actual cart URL