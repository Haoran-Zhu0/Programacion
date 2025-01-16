#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.

var1=int(input("Introduce un número:"))
var2=0

while var2<40:
    var2=var1+var2
    print(var2)
    if var2>=40:
        print("Fin de programa")

