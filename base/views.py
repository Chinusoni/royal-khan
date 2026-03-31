from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Product, RecentUpdate

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def all_products(request):
    # Grabs all products from the database, newest first
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'all_product.html', {'products': products})

def machine_detail(request, pk):
    # Safely grabs the product or returns a 404 error if it doesn't exist
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'machine_detail.html', {'product': product})

# views.py

def recent_products(request):
    # Grabs the 4 most recently added products
    recent_items = Product.objects.all().order_by('-created_at')[:4] 
    return render(request, 'recent_products.html', {'products': recent_items})

def recent_products(request):
    # Now orders by the exact moment you last clicked 'Save' in the admin
    recent_items = Product.objects.all().order_by('-updated_at')[:4] 
    return render(request, 'recent_products.html', {'products': recent_items})

def recent_products(request):
    # 1. Grab the new updates from the database
    updates_list = RecentUpdate.objects.all().order_by('-created_at') 
    
    # 2. Send them to the HTML using the dictionary key 'updates'
    return render(request, 'recent_products.html', {'updates': updates_list})