from django.db import models
from django.conf import settings

# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=20)

class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.TextField()