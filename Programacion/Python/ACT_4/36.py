#Programa que sume los n primeros números naturales. n Lo introduce el usuario.

var1=int(input("Introduce un numero:"))
total=0
for contador in range(var1):
    total=total+contador+1
print(total)