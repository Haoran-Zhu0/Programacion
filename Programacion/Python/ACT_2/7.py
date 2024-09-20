#Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?

var1=int(input("introduce el primer numero:"))
var2=int(input("introduce el segundo numero:"))
var_s=var1+var2
var_r=var1-var2
var_multi=var1*var2
var_divi=var1/var2
var_expo=var1**var2
var_divi_entera=var1//var2
print("la suma de",(var1),"y",(var2),"es",var_s)
print("la resta de",(var1),"y",(var2),"es",var_r)
print("la multiplicacion de",(var1),"y",(var2),"es",var_multi)
print("la division de",(var1),"y",(var2),"es","{:.2f}".format(var_divi))
print("el exponente de",(var1),"y",(var2),"es",var_expo)
print("la division entera de",(var1),"y",(var2),"es",var_divi_entera)
