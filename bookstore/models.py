from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(default=0)
    isbn = models.CharField(max_length=6)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
