#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista.

lista=[]
seguir=True

vocales={'à','è','ì','ò','ù','á','é','í','ó','ú'}

while seguir:
    letra=input("Introduce una letra: ").lower()

    if not letra.isdigit() and letra not in vocales:
        if letra not in lista:
            lista.append(letra)

    repetir=input("¿Deseas repetir s/n: ").lower()
    if repetir=='n':
        seguir=False

print(lista)
