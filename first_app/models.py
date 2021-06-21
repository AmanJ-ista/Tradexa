from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post_1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    text=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)


