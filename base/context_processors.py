from .models import Product

def recent_updates_processor(request):
    # This variable 'recent_sidebar_products' will be available in ALL templates
    return {
        'recent_sidebar_products': Product.objects.all().order_by('-created_at')[:3]
    }