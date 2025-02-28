#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

lista_1=[]
lista_2=[]
var1=0
var1=int(input("Introduce las veces de numeros que quieres introduir:"))
for contador in range(0,var1):
    lista_1.append(input("Introduce una palabra:"))
lista_1.sort()    
lista_2=lista_1.copy()
lista_2.sort(reverse=True)
print(lista_1)
print(lista_2)