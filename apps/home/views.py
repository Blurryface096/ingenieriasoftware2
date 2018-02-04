from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.home.models import Preguntas
from django.contrib.auth.forms import UserCreationForm
from apps.home.models import JuegoForm
from apps.home.models import Juego
from apps.home.models import Jugador
from apps.home.models import Demarcacion
from django.contrib.auth.models import User
from apps.home.models import Partido
from apps.home.models import Formaciones
from apps.home.models import ParticipacionPolla
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required(login_url='')
def home(request):
    nombre=request.user.username

    juego=Juego.objects.all()
    return render(request, 'home/home.html', { 'juego': juego, 'user':nombre})

@login_required(login_url='')
def trivia(request):
    preguntas = Preguntas.objects.all()
    return render(request, 'home/trivia.html', { 'preguntas': preguntas})

def crear_juego(request):
    if request.method=='POST':
        form=JuegoForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.organizador=request.user
            instance=form.save(commit=True)

            #for User in instance.invitados['invitados']:
            #    instance.invitados.add(User)
            instance.save()
            cadena='home:' + str(instance.tipo).lower()
            return redirect('home:polla', instance.id)
            #return redirect(cadena(instance),instance)
    else:
        form=JuegoForm()
    return render(request, 'home/crear_juego.html', {'form':form})

def jugadores(request, formacion_id):
    if request.method == 'POST':
        rawform = request.body
        params = str(rawform).split('&')
        print(params)
        jugadores = []
        for i in range(0, len(params)):
            if 'jugador' in params[i]:
                old = params[i].split('=')[1]
                n1 = old.replace("'","")
                n2 = n1.replace('"','')
                jugadores.append(int(n2))

        ataque = 0
        defensa = 0
        velocidad = 0
        for j in jugadores:
            jugador = Jugador.objects.get(id=j)
            ataque = ataque + jugador.ataque
            defensa = defensa + jugador.defensa
            velocidad = velocidad + jugador.velocidad

        ataque_medio = round(ataque/11, 3)
        print(ataque_medio)
        defensa_media = round(defensa/11, 3)
        print(defensa_media)
        velocidad_media = round(velocidad/11, 3)
        print(velocidad_media)

        total = round((ataque_medio + defensa_media + velocidad_media) / 3, 3)
        print(total)

        contexto = {'ataque_medio' : ataque_medio,
        'defensa_media' : defensa_media,
        'velocidad_media' : velocidad_media,
        'total' : total }
        return render(request, 'equipoideal/resultados.html', contexto)
    else:
        formacion = Formaciones.objects.get(id=formacion_id)
        jugadores = Jugador.objects.all().order_by('id')
        arqueros = []
        defensas = []
        centrocampistas = []
        delanteros = []
        arquero = Demarcacion.objects.get(nombre='ARQUERO')
        defensa = Demarcacion.objects.get(nombre='DEFENSA')
        centrocampista = Demarcacion.objects.get(nombre='CENTROCAMPISTA')
        for jugador in jugadores:
            if jugador.demarcacion == arquero:
                arqueros.append(jugador)
            elif jugador.demarcacion == defensa:
                defensas.append(jugador)
            elif jugador.demarcacion == centrocampista:
                centrocampistas.append(jugador)
            else:
                delanteros.append(jugador)

        lst_defs = []
        print('cantidad de defensas: {}'.format(formacion.cantidad_defensas))
        cant_defs = formacion.cantidad_defensas
        for i in range(0, cant_defs):
            lst_defs.append(defensas)

        lst_cent = []
        print('cantidad de centros: {}'.format(formacion.cantidad_centrocampistas))
        for j in range(0, formacion.cantidad_centrocampistas):
            lst_cent.append(centrocampistas)

        lst_dela = []
        for k in range(0, formacion.cantidad_delanteros):
            lst_dela.append(delanteros)

        contexto = {'formacion' : formacion, 'arqueros' : arqueros,
        'lst_defs' : lst_defs, 'lst_cent' : lst_cent,
        'lst_dela' : lst_dela}

        return render(request, 'equipoideal/jugadores.html', contexto)



def polla(request):
    juego=request.GET['juego',False]
    partidos = Partido.objects.all().order_by('id')
    contexto = {'partidos' : partidos}
    if request.method == 'POST':
        score = 0
        form = request.POST
        longitud = len(form)-1
        for x in range(0, longitud):
            i=form['a_partido_id={}'.format(x+1)]
            if i == str(partidos[x].resultado):
                score = score + 1
        user = request.user
        fecha = datetime.datetime.now()
        formatedDate = fecha.strftime("%Y-%m-%d %H:%M:%S")
        participacion = ParticipacionPolla(usuario=user, score=score, fecha=formatedDate, juego=juego)
        participacion.save()
        return redirect('login:resultados', score)
    else:
        return render(request, 'polla/polla.html', contexto)

def resultados(request, score):
    partidos = Partido.objects.all().order_by('id')
    contexto = {'score' : score, 'partidos' : partidos}
    return render(request, 'polla/resultados.html', contexto)

def formaciones(request):
    if request.method == 'POST':
        formacion_id =  request.POST.__getitem__('formacion')
        return redirect('home:jugadores', formacion_id)
    else:
        formaciones = Formaciones.objects.all()
        contexto = {'formaciones' : formaciones}
        return render(request, 'equipoideal/formacion.html', contexto)
