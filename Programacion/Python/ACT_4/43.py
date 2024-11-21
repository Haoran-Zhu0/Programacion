#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra.
var1=input("Introduce una palabra:")
var2=0
for vuelta in var1:
    var2=var2+1
    print(f"En la posicion{var2} está la {vuelta}")
