from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'home.html')

# Add this function
def machine_info(request):
    return render(request, 'machine_detail.html')

def all_products(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'all_products.html', {'products': products})

def machine_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'machine_detail.html', {'product': product})

def all_products(request):
    products = Product.objects.all().order_by('-created_at')
    # Change it here to match your file name exactly
    return render(request, 'all_product.html', {'products': products})