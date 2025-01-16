#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
numero_secreto=random.randint(1,5)
var1=False
while var1==False:
    var2=int(input("Introduce un número entre 1 y 5:"))
    if var2==numero_secreto:
        print("Has acertado")
        var1=True
    else:
        print("No has acertado")
