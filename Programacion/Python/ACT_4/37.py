#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.

var1=int(input("Introduce el número de notas que deseas introducir:"))
for contador in range(var1):
    var2=float(input("Introduce la nota:"))
    if var2>5:
        print("Asignatura aprobada")
    elif var2<5:
        print("Asignatura suspendida")