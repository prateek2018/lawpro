from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User)
    pic=models.FileField(upload_to='pic')
    


class register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)  
	
    def __str__(self):
        return self.fname

