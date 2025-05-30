from django.db import models
from django.core.validators import MaxLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField()
    documentation_url = models.URLField(max_length=60, validators=[MaxLengthValidator(15)])
    auth_required = models.BooleanField()
    additional_info = models.JSONField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
