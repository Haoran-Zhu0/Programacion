#A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While

contador=0
veces=int(input("Introduce las veces que quieras que se repita:"))
while contador<veces:
    print("Buenos dias")
    contador+=1
