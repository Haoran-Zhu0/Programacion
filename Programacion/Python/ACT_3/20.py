#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#numeros entre 0 y 10

var1=int(input("introduce un valor:"))
var2=int(input("introduce otro valor:"))

if var1>10 or var2>10:
    print(f"uno o los dos numeros estan fuera del limite establecido")

elif var1>var2:
    print(f"el {var1} es mayor que el {var2}")
elif var1<var2:
    print(f"el {var1} es menor que el {var2}")
elif var1==var2:
    print(f"el {var1} es igual que el {var2}")
