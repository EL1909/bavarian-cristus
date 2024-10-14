from django.db import models
from django.contrib.auth.models import User


class ImagePost(models.Model):
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_images')
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.Charfield(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=255)





class Comment(models.Model):
    text = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
