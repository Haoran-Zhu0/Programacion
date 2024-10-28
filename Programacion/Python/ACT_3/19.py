#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales.

var1=int(input("introduce un valor:"))
var2=int(input("introduce otro valor:"))

if var1>var2:
    print(f"el {var1} es mayor que el {var2}")
if var1<var2:
    print(f"el {var1} es menor que el {var2}")
if var1==var2:
    print(f"el {var1} es igual que el {var2}")
