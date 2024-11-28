#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
var1=input("Introduce una palabra:")
vocales=""
consonante=""

for letra in var1:
    if letra in "aeiouáéíóú":
        vocales+=letra
    elif letra.isalpha():
        consonante+=letra
print(f"Las vocales de la palabra abrigo son:{vocales}")
print(f"Las consonantes de la palabra abrigo son:{consonante}")