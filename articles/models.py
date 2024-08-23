from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title=models.TextField()
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    publish=models.DateField(auto_now_add=False,auto_now=True)