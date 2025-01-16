#Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While


var1=int(input("Introduce un numero:"))
var2=int(input("Introduce otro numero:"))
var_suma=var1+var2
print(var_suma)
var_pregunta=int(input("¿Quieres repetir la operacion?(1=si,2=no):"))
while var_pregunta==1:
    var1=int(input("Introduce un numero:"))
    var2=int(input("Introduce otro numero:"))
    var_suma=var1+var2
    print(var_suma)
    var_pregunta=int(input("¿Quieres repetir la operacion?(1=si,2=no):"))
else:
    print("Programa finalizado")