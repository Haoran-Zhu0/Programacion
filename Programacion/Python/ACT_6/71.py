#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.

lista=[]
seguir=True

while seguir:
    letra=input("Introduce una letra: ")
    
    if not letra.isdigit():
        if letra not in lista:
            lista.append(letra)

    repetir=input("¿Deseas repetir s/n: ").lower()
    if repetir=='n':
        seguir=False

print(lista)
