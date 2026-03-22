from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Existing main image
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # NEW: Extra images
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # NEW: Video link (e.g., YouTube)
    video_url = models.URLField(blank=True, null=True, help_text="Paste YouTube embed URL here")
    
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title