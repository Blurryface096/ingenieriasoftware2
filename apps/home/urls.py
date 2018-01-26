from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.home.views import home
from apps.home.views import trivia
from . import views
app_name = 'home'
urlpatterns = [
    path('', home, name='index'),
    url(r'^trivia$',views.trivia)
]
