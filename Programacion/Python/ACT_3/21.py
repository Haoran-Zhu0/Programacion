a=int(input("Introduce el primer valor:"))
b=int(input("Introduce el segundo valor:"))
c=int(input("Introduce el tercer valor:"))
import math
divi=2*a
var1=b**2-4*a*c
sqrt=math.sqrt
if var1>0:
    var2=-b+math.sqrt(var1)
    var3=-b-math.sqrt(var1)
    x1=var2/divi
    x2=var3/divi
    print("El valor de x1 es",x1)
    print("El valor de x2 es",x2)
if var1<0:
    print("La raíz no puede ser un valor negativo")