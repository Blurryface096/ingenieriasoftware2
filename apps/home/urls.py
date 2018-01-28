from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.home.views import home
from apps.home.views import trivia
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'home'
urlpatterns = [
    path('', login_required(home), name='index'),
    url(r'^trivia$',login_required(views.trivia))
]
