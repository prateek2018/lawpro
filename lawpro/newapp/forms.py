from django import *
from django.contrib.auth.models import User
from .models import *

class Myform(forms.ModelForm):
    pic=forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password',
                'confirm_password']
        
