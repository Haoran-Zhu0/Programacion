#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 

import random
import time

var1=0
var2=0
var3=0
var4=0
var5=0
var6=0

inicio=time.time()
while time.time()-inicio<3:
    numero=random.randint(1,6)
    if numero==1:
        var1+=1
    if numero==2:
        var2+=1
    if numero==3:
        var3+=1
    if numero==4:
        var4+=1
    if numero==5:
        var5+=1
    if numero==6:
        var6+=1
      
print(f"Uno: {var1}")
print(f"Dos: {var2}")
print(f"Tres: {var3}")
print(f"Cuatro: {var4}")
print(f"Cinco: {var5}")
print(f"Seis: {var6}")
