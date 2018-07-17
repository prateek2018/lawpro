from django import *
from .models import *

class Myform(forms.ModelForm):
    class Meta:
        model=consultation
        fields='__all__'
        

