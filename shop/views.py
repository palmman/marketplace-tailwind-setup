
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .models import Product
from django.utils.text import slugify

from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegisterForm, AddProductForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def home(request):
    
    products = Product.objects.all().order_by('-created')[:8]
    
    context = {
        'products':products,
    }
    return render(request, 'home.html', context)

def shop(request):
    
    products = Product.objects.all().order_by('-created')
    

    context = {
        'products':products,
    }
    return render(request, 'shop.html', context)

def product(request, category_slug, product_slug ):
    
    product =  Product.objects.get(category__slug=category_slug, slug=product_slug)
    
    context = {
        'product':product,
    }
    
    return render(request, 'product.html', context)

def category(request, category_slug=None ):
    
    category = None
    products = None
    
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category).order_by('-created')
    else:
        products = Product.objects.all().order_by('-created')
    
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'product_category.html', context)


def register(request):
    

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, first_name=first_name, last_name=last_name, password=password )
            user.save()
            auth.login(request, user)
            return redirect('home')
        
    else:
        form = RegisterForm()
        
    context = {
        'form':form,
    }
        
    return render(request, 'register.html', context)

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect.')
        
        
    return render(request, 'login.html')

def logout(request):
    
    auth.logout(request)
    
    return redirect('login')

def search(request):
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        
        if keyword:
            
            products = Product.objects.order_by('created').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
            
    context = {
        'products':products,
    }
            
    return render(request, 'shop.html', context)

def profile(request):
    
    seller_products = Product.objects.filter(seller=request.user)
    
    context = {
        'seller_products':seller_products,
    }
    
    return render(request, 'profile.html', context)

def add_product(request):
    
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            add_product = form.save(commit=False)
            add_product.seller = request.user
            add_product.slug = slugify(add_product.name)
            add_product.save()
            print(add_product)
            return redirect('profile')
            
    else:
       form = AddProductForm()
       
    context = {
        'form': form,
    }        
        
    return render(request, 'add_product.html', context)
    

