from django.shortcuts import *
from django.http import *
from django.contrib import auth
from .forms import *
from .models import *

# Create your views here.

def login (request):
    return render(request,'login.html')

	
def index(request):
    return render(request,'practice1.html')

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

def sign(request):

    if request.method=='POST':
        form=Myform(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            u=User.objects.create_user(first_name=cd['first_name'],
                                     last_name=cd['last_name'],
                                     username=cd['username'],
                                      
                                     email=cd['email'],
                                     password=cd['password'])
            
            p=profile(user=u,pic=form.cleaned_data['pic'],cc_no=form.cleaned_data['cc_no'])
            
            p.save()
            return redirect('login_app:login')
            
        
    else:
        form=Myform()

    return render(request,'sign.html',{'form':form})

def auth_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,
                           password=password)
    if user is not None:
        auth.login(request,user)
        
        return redirect('login_app:index')
    else:
        return redirect('login_app:login')
        

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

    
    
