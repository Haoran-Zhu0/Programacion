#Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
numero_secreto=random.randint(1, 5)
intentos=3
while intentos>0:
    var1=int(input(f"Te quedan {intentos} intentos.Introduce un número entre 1 y 5:"))
    if var1==numero_secreto:
        print("Has acertado")
        break
    else:
        print("No has acertado")
    intentos-=1
if intentos==0:
    print("Se te han acabado los intentos")
