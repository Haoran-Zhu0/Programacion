#Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla.

var1=input("introduce una letra:")
l=var1.isupper()
n=var1.isnumeric()
if n==True:
    print("El valor introducido es un numero")
    
if l==False and n==False:
    print("Es minuscula")
if l==True:
    print("Es mayuscula")
