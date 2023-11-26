from django.db import models
from django_resized import ResizedImageField
# Create your models here.

class Stuff(models.Model):
    name = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=40, blank=True)
    profile_pic = ResizedImageField(size=[400, 400], quality=100, upload_to="stuff", default="defaults/default_profile_pic.jpg", null=True, blank=False)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name