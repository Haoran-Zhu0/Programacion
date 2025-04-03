#Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?

import random

lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
valor_ran=random.choice(lista)
var=0
var1=""

print(lista)
var=int(input("Introduzca cuantas partidas quiere hacer: "))
for x in range
var1=input("Introducir un valor de la lista: ")

    
    if var1==valor_ran:
        print("ACERTASTE")
        
    else:
        print("SIGUE JUGANDO")
        var=input("Introducir un valor de la lista: ")
