#Utilizando listas,crea un programa que te permita determinar si un número es decimal o no. 

var1=["12","12.1","Hola","12.","6.098","6.09a","4.34.2"]

for x in var1:
    if '.' in x and x.isnumeric()==False:
        print("Es un número con decimales")
    else:
        print("No es un número con decimales")
