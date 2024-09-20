#programa que pida un número de horas y muestre por pantalla los minutos y segundos

var1=int(input("introduce un numero  entero de segundos:"))
var_min=var1/60
var_hora=var1/3600
print("el numero de minutos es","{:.2f}".format(var_min),"y en horas es","{:.5f}".format(var_hora))
