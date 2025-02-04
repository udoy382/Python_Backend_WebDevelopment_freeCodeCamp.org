from django.db import models

# Create your models here.

# username = admin
# password = admin 

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name