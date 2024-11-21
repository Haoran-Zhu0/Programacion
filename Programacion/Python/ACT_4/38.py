#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10.

var1=int(input("Introduce el número de notas que deseas introducir:"))
if var1<0 or var1>10:
    print("Error el número tiene que ser inferiores a 0 y superiores a 10")
else:
    
    for contador in range(var1):
        var2=float(input("Introduce la nota:"))
        if var2>=5:
            print("Asignatura aprobada")
        elif var2<5:
            print("Asignatura suspendida")