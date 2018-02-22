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
