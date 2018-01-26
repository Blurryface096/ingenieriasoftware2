from django.contrib import admin
from django.urls import path
from apps.home.views import home
app_name = 'home'
urlpatterns = [
    path('', home, name='index'),
    url(r'^trivia$', view.trivia),
]
