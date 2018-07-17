from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User)
    pic=models.FileField(upload_to='pic')
    cc_no=models.CharField(max_length=30)
    lstdate=models.CharField(max_length=30,null=True)
    nxtdate=models.CharField(max_length=30,null=True)
    '''
    def __str__(self):
        
        return cc_no
'''

