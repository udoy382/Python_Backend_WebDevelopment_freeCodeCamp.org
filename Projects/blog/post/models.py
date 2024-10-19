from django.db import models
from datetime import datetime


# Create your models here.


# username = admin
# password = admin

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=10000000)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)