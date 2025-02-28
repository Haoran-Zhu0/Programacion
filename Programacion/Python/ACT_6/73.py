#Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no.

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
var1=[]
var2=[]

for palabra in lista2:
    if palabra in lista1:
        var1.append(palabra)
    else:
        var2.append(palabra)

print("Están repetidas:", var1)
print("No están repetidas:", var2)
