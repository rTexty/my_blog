from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length =80, default = '')
    post_image = models.ImageField(upload_to ='blog_images/')
    post_text = models.TextField(max_length =300)
    posted_date = models.DateTimeField(default=timezone.now)