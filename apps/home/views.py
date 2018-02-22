from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from apps.home.models import Preguntas
from django.contrib.auth.forms import UserCreationForm
from apps.home.models import JuegoForm
from apps.home.models import Juego
from apps.home.models import Jugador
from apps.home.models import Demarcacion
from django.contrib.auth.models import User
from apps.home.models import Partido
from apps.home.models import Formaciones
from apps.home.models import ParticipacionPolla,ParticipacionEquipoIdeal,ParticipacionTrivia,BalanceMonetarioForm,BalanceMonetario,PreguntasTrivia
from django.contrib.auth.decorators import login_required
import datetime
import random
from django.template import RequestContext
from django.contrib import messages
from django.conf import settings
from apps.home.funciones import obtener_score,obtener_cadena,obtener_namespace,obtener_aleatorios,obtener_secuencias
# Create your views here.


def analitica(request):
    return render(request, 'home/analytics.html')

def ayuda(request):
    return render(request, 'home/ayuda.html')

def home(request):
    nombre=request.user.username


    #cadena="{% static 'img/c" +  str(k)  + ".png' %}"

    balance=BalanceMonetario.objects.get(usuario=request.user).balance
    juego=Juego.objects.filter(invitados=request.user)
    k=len(juego)
    cadena=obtener_cadena(k)

    juego2=Juego.objects.filter(privacidad='Publico')
    if balance:
        balance=balance
    else:
        balance=0

    listajuego=list(set(list(juego)+list(juego2)))
    return render(request, 'home/home.html', { 'juego': listajuego, 'user':nombre,'balance':balance, 'cadena':cadena})

def notificaciones(request):
    nombre=request.user.username


    juego=Juego.objects.filter(invitados=request.user)



    return render(request, 'home/notificaciones.html', { 'juego': juego, 'user':nombre})

def crear_juego(request):
    if request.method=='POST':
        form=JuegoForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.organizador=request.user
            instance.estado='Abierto'
            instance.n=0


            instance.pozo=instance.costo*instance.n_jugadores

            objetobalance=BalanceMonetario.objects.get(usuario=request.user)
            if objetobalance and objetobalance.balance>=instance.costo:
                objetobalance.balance=objetobalance.balance-instance.costo
                objetobalance.save()

                instance=form.save(commit=True)
                instance.save()
            else:
                messages.success(request, "Not Enough Minerals")
                return redirect('home:index')

            if request.user!=instance.invitados:
                instance.invitados.add(request.user)
            instance.save()
            #for User in instance.invitados['invitados']:
            #    instance.invitados.add(User)

            namespace='home:polla'

            #cadena='home:' + str(instance.tipo).lower()
            if str(instance.tipo).lower()=='polla':
                namespace='home:polla'
            elif str(instance.tipo).lower()=='trivia':
                namespace='home:trivia'
            elif str(instance.tipo).lower()=='equipo':
                namespace='home:equipo'
            else:
                namespace='home:polla'

            preguntastriv=[]
            if namespace=='home:trivia':
                temp=Preguntas.objects.all().order_by('id')
                preguntas=obtener_aleatorios(temp)
                preguntastriv = PreguntasTrivia(juego=instance)
                for p in preguntas:
                    preguntastriv.preguntas_juego.add(p)

                preguntastriv.save()


            return redirect(namespace, instance.id)
            #return redirect(cadena(instance),instance)
    else:
        form=JuegoForm()
    return render(request, 'home/crear_juego.html', {'form':form})


def entrar_juego(request,juego):
    id_jug=juego
    #tipo_jug=tipo
    tipo_jug=Juego.objects.get(id=id_jug).tipo.lower()
    juego=Juego.objects.get(id=id_jug)



    namespace=obtener_namespace(tipo_jug)
    condicion=False
    objetos=[]
    if tipo_jug == 'polla':
        objetos = ParticipacionPolla.objects.all()

    elif tipo_jug == 'equipo':
        objetos = ParticipacionEquipoIdeal.objects.all()
    else:
        objetos = ParticipacionTrivia.objects.all()

    for o in objetos:
        if o.usuario==request.user and o.juego==juego:
            condicion=True
            break

    if condicion:
        messages.success(request, "Ya jugaste este juego")
        return redirect('home:index')
    else:
        objetobalance=BalanceMonetario.objects.get(usuario=request.user)
        if objetobalance and objetobalance.balance>=juego.costo:
            objetobalance.balance=objetobalance.balance-juego.costo
            objetobalance.save()
            return redirect(namespace, id_jug)
        else:
            messages.success(request, "Not Enough Minerals")
            return redirect('home:index')

def jugadores(request, cadena):
    division=cadena.split('&')

    formacion_id=int(division[0])
    jug_id=int(division[1])
    juego=Juego.objects.get(id=jug_id)
    if request.method == 'POST':
        rawform = request.body
        params = str(rawform).split('&')

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

        defensa_media = round(defensa/11, 3)

        velocidad_media = round(velocidad/11, 3)


        score = obtener_score(ataque_medio,defensa_media,velocidad_media)




        contexto = {'ataque_medio' : ataque_medio,
        'defensa_media' : defensa_media,
        'velocidad_media' : velocidad_media,
        'score' : score,
        'juego':juego }
        user = request.user
        fecha = datetime.datetime.now()
        formatedDate = fecha.strftime("%Y-%m-%d %H:%M:%S")
        participacion = ParticipacionEquipoIdeal(usuario=user, ataque=ataque_medio, defensa=defensa_media,
        velocidad=velocidad_media,score=score, fecha=formatedDate, juego=juego)
        participacion.save()

        juego.n += 1
        if juego.n >= juego.n_jugadores:
            participaciones=ParticipacionEquipoIdeal.objects.filter(juego=juego)
            max=0
            ganadores=[]
            for i in participaciones:
                if i.score>max:
                    max=i.score
            for i in participaciones:
                if i.score==max:
                    ganadores.append(i.usuario)
            for j in ganadores:
                balancemonetario=BalanceMonetario.objects.get(usuario=j)
                balancemonetario.balance=balancemonetario.balance+juego.pozo/len(ganadores)
                balancemonetario.save()
            juego.estado='Cerrado'
        juego.save()

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



def polla(request, juego):
    #juego=request.POST.get('juego')
    juego=Juego.objects.get(id=juego)
    partidos = Partido.objects.all().order_by('id')
    contexto = {'partidos' : partidos}
    if request.method == 'POST':
        score = 0
        form = request.POST
        longitud = len(form)-1
        for x in partidos:
            i=form['a_partido_id={}'.format(x.id)]
            if i == str(x.resultado):
                score = score + 1
        user = request.user
        fecha = datetime.datetime.now()
        formatedDate = fecha.strftime("%Y-%m-%d %H:%M:%S")
        participacion = ParticipacionPolla(usuario=user, score=score, fecha=formatedDate, juego=juego)
        participacion.save()
        juego.n += 1
        if juego.n >= juego.n_jugadores:
            participaciones=ParticipacionPolla.objects.filter(juego=juego)
            max=0
            ganadores=[]
            for i in participaciones:
                if i.score>max:
                    max=i.score
            for i in participaciones:
                if i.score==max:
                    ganadores.append(i.usuario)
            for j in ganadores:
                balancemonetario=BalanceMonetario.objects.get(usuario=j)
                balancemonetario.balance=balancemonetario.balance+juego.pozo/len(ganadores)
                balancemonetario.save()
            juego.estado='Cerrado'
        juego.save()
        cadena=str(score)+'&'+str(juego.id)
        return redirect('home:resultados', cadena)
    else:
        return render(request, 'polla/polla.html', contexto)

def resultados(request, cadena):
    preguntas = Preguntas.objects.all().order_by('id')
    division=cadena.split('&')

    score=int(division[0])
    jug_id=int(division[1])
    juego=Juego.objects.get(id=jug_id)
    partidos = Partido.objects.all().order_by('id')
    contexto = {'score' : score, 'partidos' : partidos,'juego':juego}

    return render(request, 'polla/resultados.html', contexto)

def formaciones(request, juego):
    if request.method == 'POST':
        formacion_id =  request.POST.__getitem__('formacion')


        cadena=str(formacion_id)+'&'+str(juego)
        return redirect('home:jugadores', cadena)
    else:

        formaciones = Formaciones.objects.all()
        contexto = {'formaciones' : formaciones}
        return render(request, 'equipoideal/formacion.html', contexto)


def preguntas(request, cadena):
    if request.method == 'POST':
        pregunta_id =  request.POST.__getitem__('pregunta')


        cadena=str(pregunta_id)+'&'+str(juego)
        return redirect('home:trivia_juego', cadena)
    else:

        listapreg = Preguntas.objects.all()
        if len(listapreg)>10:
            while len(preguntas)<10:
                for i in listapreg:
                    num=random.randrange(1,3)
                    if num==2:
                        preguntas.add(i)
                        listapreg.remove(i)
                    if len(preguntas)==10:
                        break
        else:
            preguntas=listapreg
        contexto = {'Preguntas' : preguntas}
        return render(request, 'trivia/preguntas.html', contexto)


def modificar_balance(request):
    balance=BalanceMonetario.objects.get(usuario=request.user).balance
    if request.method=='POST':
        form=BalanceMonetarioForm(request.POST,request.FILES)
        if form.is_valid():
            agregado=float(request.POST.get("agregar_cant"))
            instance=form.save(commit=False)
            instance.usuario=request.user
            instance.balance=balance+agregado
            instance=form.save(commit=True)
            instance.save()

            messages.success(request, "Cantidad Agregada")
            return redirect('home:index')

    else:
        form=BalanceMonetarioForm()
    contexto = {'form' : form,'balance':balance}
    return render(request, 'balance/cuenta.html', contexto)



def trivia_juego(request,juego):
    juego=Juego.objects.get(id=juego)
    #Book.objects.all().order_by('?')[:10]
    temp=Preguntas.objects.all().order_by('id')
    listapreg=[]
    for k in temp:
        listapreg.append(k)
    preguntas=[]
    if len(listapreg)>10:
        while len(preguntas)<10:
            for i in listapreg:
                num=random.randrange(1,3)
                if num==2:
                    preguntas.append(i)
                    listapreg.remove(i)
                if len(preguntas)==10:
                    break
    else:
        preguntas=listapreg

    preguntas=PreguntasTrivia.objects.get(juego=juego).preguntas_juego.order_by('id')
    contexto = {'preguntas' : preguntas,'juego':juego}

    if request.method == 'POST':
        score = 0
        form = request.POST
        longitud = len(form)-1


        for x in preguntas:
            i=form['p{}'.format(x.id)]
            if i == str(x.respuesta):
                score = score + 1


        user = request.user
        fecha = datetime.datetime.now()
        formatedDate = fecha.strftime("%Y-%m-%d %H:%M:%S")
        participacion = ParticipacionTrivia(usuario=user, score=score, fecha=formatedDate, juego=juego)
        participacion.save()
        juego.n += 1
        if juego.n >= juego.n_jugadores:
            participaciones=ParticipacionTrivia.objects.filter(juego=juego)
            max=0
            ganadores=[]
            for i in participaciones:
                if i.score>max:
                    max=i.score
            for i in participaciones:
                if i.score==max:
                    ganadores.append(i.usuario)
            for j in ganadores:
                balancemonetario=BalanceMonetario.objects.get(usuario=j)
                balancemonetario.balance=balancemonetario.balance+juego.pozo/len(ganadores)
                balancemonetario.save()
            juego.estado='Cerrado'
        juego.save()
        cadena=str(score)+'&'+str(juego.id)
        return redirect('home:resultadostrivia', cadena)
    else:
        return render(request, 'home/trivia.html', contexto)

def resultadostrivia(request, cadena):

    division=cadena.split('&')

    score=int(division[0])
    jug_id=int(division[1])
    juego=Juego.objects.get(id=jug_id)
    preguntas=PreguntasTrivia.objects.get(juego=juego).preguntas_juego.order_by('id')
    contexto = {'score' : score, 'preguntas' : preguntas, 'juego':juego}

    return render(request, 'home/resultadostrivia.html', contexto)


def puntuaciones(request, id_juego):
    if request.method == 'GET':
        juego = Juego.objects.get(id=id_juego)
        if juego.tipo == 'Polla':
            participaciones = ParticipacionPolla.objects.filter(juego=juego).order_by('-score')

        elif juego.tipo == 'Equipo':
            participaciones = ParticipacionEquipoIdeal.objects.filter(juego=juego).order_by('-score')
        else:
            participaciones = ParticipacionTrivia.objects.filter(juego=juego).order_by('-score')
        contexto = {'participaciones' : participaciones, 'titulo' : juego.nombre}
        return render(request, 'home/posiciones.html', contexto)
    else:
        pass


def descartar(request, id_juego):
    if request.method == 'GET':
        juego = Juego.objects.get(id=id_juego)
        juego.invitados.remove(request.user)
        juego.save()
        nombre=request.user.username
        juego=Juego.objects.filter(invitados=request.user)

        return render(request, 'home/notificaciones.html', { 'juego': juego, 'user':nombre})
    else:
        pass
