from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=512, null=False)
    desription = models.CharField(max_length=1024)
    author = models.CharField(max_length=64)
    year = models.CharField(max_length=32, null=True, default="1984")
    read = models.BooleanField(default=False)
