from django.contrib import admin
# Add RecentUpdate to this import line below!
from .models import Product, RecentUpdate 
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'created_at') 
    list_filter = ('created_at',) 
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    
    thumbnail.short_description = 'Preview'

# --- THE NEW RECENT UPDATES SECTION ---
@admin.register(RecentUpdate)
class RecentUpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)