#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.

import random

numero_secreto=random.randint(0, 1000)
intentos=0
var1=False
while not var1:
    var2=int(input("Introduce un número:"))
    intentos+=1
    if var2<numero_secreto:
        print("El número es mayor que",var2)
    elif var2>numero_secreto:
        print("El número es menor que",var2)
    else:
        var1=True
        print(f"Acertastes, has realizado {intentos} intentos.")
