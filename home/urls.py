from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
  path("",views.index,name='home'),
  path("index.html",views.index,name='home'),

    
]