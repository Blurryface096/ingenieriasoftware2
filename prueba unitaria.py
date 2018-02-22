from apps.home.funciones import obtener_score,obtener_cadena,obtener_namespace,obtener_aleatorios,obtener_secuencias
from time import time

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
        
def probar_aleatorios():
    temp=[1]*11
    

    preguntas=obtener_aleatorios(temp)

    if len(preguntas)==10:
        print("OBTENER ALEATORIOS OK")
    else:
        print("OBTENER ALEATORIOS FALLANDO")

def probar_secuencias():
    num=10
    

    num=obtener_secuencias(num)

    if num==4.25:
        print("OBTENER SECUENCIAS OK")
    else:
        print("OBTENER SECUENCIAS FALLANDO")

def main():
    tiempo_inicial = time()
    
    print("-----------INICIO DE PRUEBAS UNITARIAS----------")
    print("")
    probar_score()
    probar_cadena()
    probar_namespace()
    probar_aleatorios()
    probar_secuencias()
    tiempo_final = time()
    print("")
    print("Terminó ejecución de pruebas unitarias en {} segundos".format(tiempo_final-tiempo_inicial))

if __name__=='__main__':
    main()
