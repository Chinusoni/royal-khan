from django.shortcuts import render, get_object_or_404
from .models import Product

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