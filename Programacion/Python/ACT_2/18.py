#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.

var1=int(input("introduce el numero de personas adultos:"))
var2=int(input("introduce el numero de personas menores:"))
p_adulto=var1*6
p_menores=var2*10.8
p_total=p_adulto+p_menores
print("Dinero pagado de adultos:",p_adulto)
print("Dinero pagado de menores:",p_menores)
print("Dinero pagado total:",p_total)
