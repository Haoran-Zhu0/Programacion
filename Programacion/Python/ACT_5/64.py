#. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos

pares=0
impares=0
positivos=0
negativos=0
suma_total=0
numero=0
while numero!=-99:
    numero=int(input("Introduce un número:"))
    if numero>0:
        positivos+=1
    else:
        negativos+=1
    if numero%2==0:
        pares+=1
    else:
        impares+=1
        
    suma_total+=numero
        
print(f"El número de pares es {pares}")
print(f"El número de impares es {impares}")
print(f"El número de positivos es {positivos}")
print(f"El número de negativos es {negativos}")
print(f"El total es {suma_total}")
