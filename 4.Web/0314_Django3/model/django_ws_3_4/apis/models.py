from django.db import models

# Create your models here.
class APIinfo(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    api_url = models.CharField(max_length=200)
    documentation_url = models.CharField(max_length=200)
    auto_required = models.BooleanField()
    created_at = models.DateTimeField()
    additional_info = models.TextField()