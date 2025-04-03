#Utilizando listas,crea un programa que te permita determinar si un número es decimal o no. 

numero=input("introduce un numero: ")
lista=numero.split(".")

if len(lista)!=2:
    print("no es decimal")
else:
    if lista[0].isnumeric() and lista[1].isnumeric():
        print("es decimal")
    else:
        print("no es decimal")
if len(lista)>2
    print("no es un numero con decimales")
