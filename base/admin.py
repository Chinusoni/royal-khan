from django.contrib import admin
from .models import Product # Import your model

# This line is what makes it appear in the sidebar
admin.site.register(Product)