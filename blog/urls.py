"""repaspartage URL Configuration

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
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^association/$', views.association,name='association'),
    url(r'^convives/$', views.convives,name='convives'),
    url(r'^aide/$', views.aide,name='aide'),
    url(r'^benevoles/$', views.benevoles,name='benevoles'),
    url(r'^membres/$', views.membres,name='membres'),
    url(r'^actualite/$', views.actualite,name='actualite'),

]
