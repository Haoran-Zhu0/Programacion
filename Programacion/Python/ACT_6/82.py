#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra.

import random

lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
valor_ran=random.choice(lista)
var=""
var1=""
print(lista)
var=input("Introducir un valor de la lista: ")
while var1==False :
    
    if var==valor_ran:
        print("ACERTASTE")
        
    else:
        print("SIGUE JUGANDO")
        var=input("Introducir un valor de la lista: ")
