from django.db import models
from datetime import datetime

# Create your models here.

# username = admin 
# password = admin 

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Message(models.Model):
    user = models.CharField(max_length=100000)
    room = models.CharField(max_length=100000)
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now(), blank=True)