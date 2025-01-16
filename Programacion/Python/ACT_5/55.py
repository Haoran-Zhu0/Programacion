#Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

total_suma=0
repeticiones=0

while total_suma<=50 or total_suma%2==0:
    var1=int(input("Introduce un numero:"))
    var2=int(input("Introduce otro numero:"))
    var_suma=var1+var2
    total_suma+=var_suma
    repeticiones+=1
    print(f"El resultado de la suma es:{var_suma}")
    if repeticiones==1:
        print(f"El total acumulado es:{total_suma} y llevas {repeticiones} operación realizada")
    else:
        print(f"El total acumulado es:{total_suma} y llevas {repeticiones} operaciones realizadas")
print("Programa finalizado")
