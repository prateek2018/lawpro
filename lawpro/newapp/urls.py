"""newproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from newapp.views import *

urlpatterns = [
    url(r'^$',login,name='login'),
    url(r'^home/$',index,name='index'),
    url(r'^civil/$',civil),
    url(r'^criminal/$',criminal),
    url(r'^prop/$',prop),
    url(r'^matrimonial/$',matrimonial),
    url(r'^corporate/$',corporate),
    url(r'^logout/$',logout,name='logout'),
    url(r'^sign/$',sign, name='sign'),
    url(r'^auth-check/$',auth_view,name='check')
]
