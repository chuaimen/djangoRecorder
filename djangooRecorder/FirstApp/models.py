from django.db import models

# Create your models here.

class Post(models.Model):
    client = models.CharField(max_length=75)
    workduty = models.TextField()
    #slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.client