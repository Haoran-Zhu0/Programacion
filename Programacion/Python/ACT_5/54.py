#Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While

total_suma=0
repeticiones=0
while total_suma<=50:
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

print("Programa finalizado.")
