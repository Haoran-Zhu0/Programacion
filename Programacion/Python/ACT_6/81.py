#A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
#lista al azar.

import random
lista=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
print(lista[random.randint(0, len(lista)-1)])
