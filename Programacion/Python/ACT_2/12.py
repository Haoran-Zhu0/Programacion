# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro

var1=int(input("introduce el valor de lado de un trapecio isosceles:"))
var2=int(input("introduce el base menor:"))
var3=int(input("introduce el base mayor:"))
var4=int(input("introduce la altura:"))
var_p=var2+var3+2*var1
var_a=(var2+var3)/2*var4
print("el perimetro es:",(var_p))
print("el area es:",(var_a))
