from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Add this line for the photo
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    # Add this for a slider toggle
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title