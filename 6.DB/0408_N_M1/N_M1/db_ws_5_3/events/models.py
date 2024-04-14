from django.db import models

# Create your models here.
        
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phon_number = models.CharField(max_length=15)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    location = models.TextField()
    participant = models.ManyToManyField(Participant, related_name='events')
    
    def __str__(self):
        return self.name