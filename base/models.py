from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Images
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # Video link
    video_url = models.URLField(blank=True, null=True, help_text="Paste YouTube embed URL here")
    
    # --- NEW: Tech Update Note ---
    update_note = models.CharField(max_length=255, blank=True, null=True, help_text="Write the new tech update here (e.g., 'Upgraded to 800W motor')")
    
    # Status and tracking
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RecentUpdate(models.Model):
    title = models.CharField(max_length=200, help_text="Headline of the update (e.g., 'New 800W Motor Added')")
    description = models.TextField(help_text="Full details of the update")
    image = models.ImageField(upload_to='recent_updates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recent Update"
        verbose_name_plural = "Recent Updates"
        
        
        
    def __str__(self):
        return self.title