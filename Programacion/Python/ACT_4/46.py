#A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.

var1=input("Introduce una palabra:")
var2=var1.lower()
vocales=""
consonante=""

for letra in var2:
    if letra in "aeiouáéíóú":
        vocales+=letra
    elif letra.isalpha():
        consonante+=letra
print(f"Las vocales de la palabra abrigo son:{vocales}")
print(f"Las consonantes de la palabra abrigo son:{consonante}")