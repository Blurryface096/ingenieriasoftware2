from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.home import views
from apps.home.views import home,crear_juego, entrar_juego,trivia_juego,resultadostrivia,modificar_balance,puntuaciones,notificaciones,descartar,analitica,ayuda

from apps.home.views import polla
from apps.home.views import jugadores
from apps.home.views import formaciones

from apps.home.views import resultados
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.models import User
from apps.home.models import Juego

from . import views
app_name = 'home'

urlpatterns = [
    path('', login_required(home), name='index'),
    #url(r'^trivia$',login_required(views.trivia),name='trivia'),
    path('trivia/<int:juego>',login_required(views.trivia_juego),name='trivia'),
    url(r'^logout$',logout_then_login,name='logout'),
    #url(r'^accounts/', include('apps.accounts.urls')),
    #url(r'^polla$',polla,name='polla'),
    #url(r'^polla/<int:Juego.id>/$',polla,name='polla'),
    #path('polla/<int:Juego.id>/', polla, name='polla'),
    path('polla/<int:juego>', polla, name='polla'),
    path('equipo/<int:juego>',formaciones,name='equipo'),
    #url(r'^equipo$',formaciones,name='equipo'),
    url(r'^crear_juego$',crear_juego,name='crear_juego'),
    #url(r'^entrar_juego/<int:juego>$',entrar_juego,name='entrar_juego'),
    path('estado_cuenta',modificar_balance,name='modificar_balance'),
    path('entrar_juego/<int:juego>/',entrar_juego,name='entrar_juego'),
    path('jugadores/<str:cadena>', jugadores, name='jugadores'),
    #path('polla/<str:username>/', polla, name='polla'),
    path('resultados/<str:cadena>/', resultados, name='resultados'),
    path('resultadostrivia/<str:cadena>/', resultadostrivia, name='resultadostrivia'),
    path('puntuaciones/<int:id_juego>/', puntuaciones, name='puntuaciones'),
    path('descartar/<int:id_juego>/', descartar, name='descartar'),
    path('notificaciones', notificaciones, name='notificaciones'),
    path('analitica', analitica, name='analitica'),
    path('ayuda', ayuda, name='ayuda'),
]
