#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

numero=int(input("Introduce un número:"))
var1=1
while var1<=10:
    resultado=numero*var1
    print(resultado)
    var1+=1
