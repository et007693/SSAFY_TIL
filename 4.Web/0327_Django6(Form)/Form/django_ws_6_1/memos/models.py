from django.db import models

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    insert_time = models.DateTimeField(auto_now = True)
    modi_time = models.DateTimeField(auto_now_add = True)