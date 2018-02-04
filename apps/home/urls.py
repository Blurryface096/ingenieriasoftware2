from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.home import views
from apps.home.views import home
from apps.home.views import trivia
from apps.home.views import polla
from apps.home.views import jugadores
from apps.home.views import crear_juego
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.models import User
from apps.home.models import Juego

from . import views
app_name = 'home'

urlpatterns = [
    path('', login_required(home), name='index'),
    url(r'^trivia$',login_required(views.trivia),name='trivia'),
    url(r'^logout$',logout_then_login,name='logout'),
    #url(r'^accounts/', include('apps.accounts.urls')),
    #url(r'^polla/<Juego:Juego>$',polla,name='polla'),
    path('polla/<int:Juego.id>', polla, name='polla'),
    url(r'^equipo$',jugadores,name='equipo'),
    url(r'^crear_juego$',crear_juego,name='crear_juego'),

    #path('jugadores/<int:formacion_id>', jugadores, name='jugadores'),
    #path('polla/<str:username>/', polla, name='polla'),
    #path('resultados/<int:score>/', resultados, name='resultados'),
]
