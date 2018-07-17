from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class consultation(models.Model):
  
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.IntegerField(null=True)
    subject=models.CharField(max_length=30)
    message=models.TextField(null=True)
    
    def __str__(self):
        return self.fname
