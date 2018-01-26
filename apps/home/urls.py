from django.contrib import admin
from django.urls import path
from apps.home.views import home
from apps.home.views import trivia
app_name = 'home'
urlpatterns = [
    path('', trivia, name='index'),
    path('/trivia', trivia),
]
