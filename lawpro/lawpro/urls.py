"""lawpro URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^practice/$',practice),
    url(r'^blog/$',blog),
    url(r'^about/$',about),
    url(r'^contact/$',contact),
    url(r'^login/',include('newapp.urls',namespace='login_app')),
    url(r'^civil/$',civil),
    url(r'^criminal/$',criminal),
    url(r'^prop/$',prop),
    url(r'^matrimonial/$',matrimonial),
    url(r'^corporate/$',corporate),
    url(r'^theunited/$',theunited),
    url(r'^counseling/$',counseling),
]+ static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
