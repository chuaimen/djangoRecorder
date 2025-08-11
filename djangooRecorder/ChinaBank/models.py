from django.db import models

# Create your models here.
class ChinaBankPost(models.Model):
    client = models.TextField()
    workduty = models.TextField()
    # slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    AA = models.ImageField(default='fallback.png', blank=True)
    BB = models.ImageField(default='fallback.png', blank=True)
    CC = models.ImageField(default='fallback.png', blank=True)
    DD = models.ImageField(default='fallback.png', blank=True)
    EE = models.ImageField(default='fallback.png', blank=True)
    FF = models.ImageField(default='fallback.png', blank=True)
    def __str__(self):
        return self.client