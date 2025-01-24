#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

var1=int(input("Introduzca un numero:"))
var2=int(input("Introduzca un numero:"))
pares=""
impares=""

if var1<var2:
    contador=var1
    for x in range(var1,var2):
        if contador%2==0:
            pares+=str(x)+"-"
        else:
            impares+=str(x)+"-"
        contador+=1    
if var1>var2:
    contador=var2        
    for x in range(var2,var1):
        if contador%2==0:
            pares+=str(x)+"-"
        else:
            impares+=str(x)+"-"
        contador+=1
       
pares=pares[0:-1]
impares=impares[0:-1]
print(pares)
print(impares)

