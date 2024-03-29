from django.db import models

# Create your models here.
class Travel(models.Model):
    location = models.CharField(max_length=20)
    plan = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()