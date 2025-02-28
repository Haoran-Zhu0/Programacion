#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
var1=[]
var2=[]

for palabra in lista2:
    if palabra in lista1:
        var1.append(palabra)

for palabra in lista1:
    if palabra not in lista2:
        var2.append(palabra)
        
for palabra in lista2:
    if palabra not in lista1 and palabra not in var2:
        var2.append(palabra)

print("Están repetidas:",var1)
print("No están repetidas:",var2)

