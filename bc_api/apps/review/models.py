from django.db import models
from apps.book.models import Book
from apps.user.models import BCUser

# Create your models here.


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(BCUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024)
    score = models.IntegerField()
