#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.

var1=int(input("introduce el diametro de un circulo:"))
var_radio=var1/2
import math
var_pi=math.pi
var_perimetro=2*var_pi*var_radio
var_area=var_pi*var_radio**2
print("El perimetro del circulo es:","{:.1f}".format(var_perimetro))
print("El area del circulo es:","{:.1f}".format(var_area))
