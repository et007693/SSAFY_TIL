from django.db import models

# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Trend(models.Model):
    name = models.TextField()
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateField(auto_now_add=True)