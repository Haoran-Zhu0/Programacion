#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 

import random

listword=""

lista_letras=[]
lista_desorden=[]
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]

valor_ran=random.choice(lista)
valor_ran="-".join(valor_ran)
lista_letras=valor_ran.split("-")

while len(lista_letras)>0:
    letra=random.choice(lista_letras)
    lista_desorden.append(letra)
    lista_letras.remove(letra)
    
print(lista_desorden)

