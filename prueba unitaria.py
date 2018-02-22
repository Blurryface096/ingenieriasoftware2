from apps.home.views import obtener_score

def probar_score():
    ataque=15
    defensa=18
    velocidad=12

    score=obtener_score(ataque,defensa,velocidad)

    if score==15:
        print("OBTENER SCORE OK")
    else:
        print("OBTENER SCORE FALLANDO")

def main():
    print("-----------INICIO DE PRUEBA UNITARIA----------")
    print("/n")
    probar_score()
    


if __name__=='__main__':
    main()
