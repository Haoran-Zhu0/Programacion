# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).

var1=int(input("introduce el valor del raiz:"))
import math
var_raiz=math.sqrt(var1)
var_divi=var_raiz/2
print("el resultado de la raiz es",(var_raiz))
print("el resultado de la divisio es",(var_divi))
