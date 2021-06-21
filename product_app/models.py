from django.db import models
from django.db.models.base import Model
from django.utils import timezone

class product(models.Model):
    name=models.CharField(max_length=50)
    weight=models.IntegerField()
    price=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

