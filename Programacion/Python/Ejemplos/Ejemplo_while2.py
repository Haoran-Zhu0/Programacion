import random
var1=random.randint(1,100)
var2=int(input("Introduce un numero entre el 1 y 100:"))
while var2!=var1:
    print("No has acertado")
    var=int(input("Introduce un numero entre el 1 y 100:"))
else:
    print("Has acertado el numero")