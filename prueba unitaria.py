from apps.home.funciones import obtener_score,obtener_cadena,obtener_namespace

def probar_score():
    ataque=15
    defensa=18
    velocidad=12

    score=obtener_score(ataque,defensa,velocidad)

    if score==15:
        print("OBTENER SCORE OK")
    else:
        print("OBTENER SCORE FALLANDO")

def probar_cadena():
    k=7
    

    cadena=obtener_cadena(k)

    if cadena=="/static/img/c7.png":
        print("OBTENER CADENA OK")
    else:
        print("OBTENER CADENA FALLANDO")

def probar_namespace():
    tipo_jug="trivia"
    

    namespace=obtener_namespace(tipo_jug)

    if namespace=="home:trivia":
        print("OBTENER NAMESPACE OK")
    else:
        print("OBTENER NAMESPACE FALLANDO")

def main():
    print("-----------INICIO DE PRUEBA UNITARIA----------")
    print("")
    probar_score()
    probar_cadena()
    probar_namespace()
    


if __name__=='__main__':
    main()
