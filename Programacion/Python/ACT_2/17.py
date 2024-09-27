#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso

var1=float(input("introduce el peso(en kg):"))
var2=float(input("introduce la estatura:"))

var_IMC=var1/var2**2
if var_IMC==25:
      print("Si pesas",(var1),"kg","y mides",(var2),"tu IMC es","{:.2f}".format(var_IMC))
if var_IMC<25:
      print("Si pesas",(var1),"kg","y mides",(var2),"tu IMC es","{:.2f}".format(var_IMC))
if var_IMC>25:
      print("Si pesas",(var1),"kg","y mides",(var2),"tu IMC es","{:.2f}".format(var_IMC),",Hay sobre peso")
