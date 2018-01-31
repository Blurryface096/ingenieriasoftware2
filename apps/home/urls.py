from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.home.views import home
from apps.home.views import trivia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

from . import views
app_name = 'home'

urlpatterns = [
    path('', login_required(home), name='index'),
    url(r'^trivia$',login_required(views.trivia),),
    url(r'^logout$',logout_then_login,name='logout'),
    #url(r'^accounts/', include('apps.accounts.urls')),
]
