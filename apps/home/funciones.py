def obtener_score(ataque_medio,defensa_media,velocidad_media):
    score=round((ataque_medio + defensa_media + velocidad_media) / 3, 3)
    return score
