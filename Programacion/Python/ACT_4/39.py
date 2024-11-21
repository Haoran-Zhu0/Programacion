#Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

var1=int(input("Introduce la cantidad de números que deseas introducir:"))
negativo=0
positivo=0
cero=0

for contador in range (var1):
    var2=int(input("Introduce un número:"))
    if var2>0:
        positivo=positivo+1
    if var2<0:
        negativo=negativo+1
    if var2==0:
        cero=cero+1
print("La cantidad de números positivos es:",positivo)
print("La cantidad de números negativos es:",negativo)
print("La cantidad de números ceros es:",cero)