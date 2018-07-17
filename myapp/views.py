from django.shortcuts import render
from django.http import *

# Create your views here.
from django.shortcuts import *
from .forms import *
from .models import *

def index(request):
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:

        form=Myform()
        
    return render(request,'index.html',{'form':form})

def practice(request):
    return render(request,'practice.html')
	
def civil(request):
    return render(request,'civil.html')

def criminal(request):
    return render(request,'criminal.html')

def corporate(request):
    return render(request,'corporate.html')

def prop(request):
    return render(request,'property.html')

def matrimonial(request):
    return render(request,'matrimonial.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
     if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
     else:
         form=Myform()
         
     return render(request,'about.html',{'form':form})

def contact(request):
    if request.method=='POST':
        form=Myform(request.POST)
        print(request.POST)
        if form.is_valid():
            print ('hello')
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=Myform()
        
    return render(request,'contact.html',{'form':form})

def theunited(request):
    return render(request,'theunited.html')

def counseling(request):
    return render(request,'counseling.html')
