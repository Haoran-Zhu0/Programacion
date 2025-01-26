#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor

pares=0
impares=0
positivos=0
negativos=0
suma_total=0
numero=int(input("Introduce un número: "))
mayor=numero
menor=numero

while numero!=-99:
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
    if numero%2==0:
        pares+=1
    else:
        impares+=1
    suma_total+=numero
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor=numero
    numero=int(input("Introduce un número: "))
print(f"El número de pares es {pares}")
print(f"El número de impares es {impares}")
print(f"El número de positivos es {positivos}")
print(f"El número de negativos es {negativos}")
print(f"El total es {suma_total}")
print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")

