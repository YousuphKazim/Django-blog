from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)

    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True
    )

     #title stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Title: {self.title}, image: {self.image}"