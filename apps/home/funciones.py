import random

def obtener_score(ataque_medio,defensa_media,velocidad_media):
    score=round((ataque_medio + defensa_media + velocidad_media) / 3, 3)
    return score

def obtener_cadena(k):
    if k<=9:
        cadena="/static/img/c"+ str(k)+".png"
    else:
        cadena="/static/img/c10.png"
    return cadena

def obtener_namespace(tipo_jug):
    namespace='home:polla'
    if tipo_jug=='polla':
        namespace='home:polla'
    elif tipo_jug=='trivia':
        namespace='home:trivia'
    elif tipo_jug=='equipo':
        namespace='home:equipo'
    else:
        namespace='home:polla'
    return namespace

def obtener_aleatorios(temp):
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
    return preguntas
