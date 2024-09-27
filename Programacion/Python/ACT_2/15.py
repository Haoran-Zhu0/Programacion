#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales

var1=int(input("introduce el valor del radio:"))
var2=int(input("introduce el valor del altura:"))
import math
var_pi=math.pi
var_a=2*var_pi*var1*var2+2*var_pi*var1**2
var_v=var_pi*var1**2*var2
print("el area del cilindro es","{:.2f}".format(var_a))
print("el volumen del cilindro es","{:.2f}".format(var_v))
