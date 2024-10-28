#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas.

var1="A quién madruga Dios ayuda"
print(var1)
var3=var1.islower()
var2=input("Introduce la palabra:")
var4=var1.islower()

if var2=="a":
    print("La palabra esta en la frase y esta en el i­ndice 1")
elif var2=="quién":
    print("La palabra esta en la frase y esta en el i­ndice 2")
elif var2=="madruga":
    print("La palabra esta en la frase y esta en el i­ndice 8")
elif var2=="dios":
    print("La palabra esta en la frase y esta en el i­ndice 16")
elif var2=="ayuda":
    print("La palabra esta en la frase y esta en el idice 21")
