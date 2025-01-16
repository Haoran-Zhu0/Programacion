#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While

total_suma=0
repeticiones=0
seguir="s"

while seguir=="s":
    var1=int(input("Introduce un numero:"))
    var2=int(input("Introduce otro numero:"))
    var_suma=var1+var2
    total_suma+=var_suma
    repeticiones+=1
    print(f"El resultado de la suma es:{var_suma}")
    seguir=input("Deseas repetir la operación s/n:").lower()

print(f"La suma total es: {total_suma}")
print(f"El número de repeticiones es: {repeticiones}")

