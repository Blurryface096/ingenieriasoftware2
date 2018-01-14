from django.contrib import admin
from django.urls import path
from apps.login.views import index, ingresar

app_name = 'login' 
urlpatterns = [
    path('', index),
    path('ingresar/', ingresar, name='ingreso'),
]
