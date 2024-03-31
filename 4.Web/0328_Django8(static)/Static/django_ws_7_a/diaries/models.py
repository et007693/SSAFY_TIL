from django.db import models

# Create your models here.
class Diary(models.Model):
    created_at = models.DateField(auto_now_add=False)
    content = models.TextField()