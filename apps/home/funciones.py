def obtener_score(ataque_medio,defensa_media,velocidad_media):
    score=round((ataque_medio + defensa_media + velocidad_media) / 3, 3)
    return score

def obtener_cadena(k):
    if k<=9:
        cadena="/static/img/c"+ str(k)+".png"
    else:
        cadena="/static/img/c10.png"
    return cadena
