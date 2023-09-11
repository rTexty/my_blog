from django.db import models
from django.utils import timezone
# Create your models here.
class Events(models.Model):
    event_image = models.ImageField(upload_to ='event_images/')
    event_text = models.CharField(max_length =300)
    event_date = models.DateTimeField(default=timezone.now)