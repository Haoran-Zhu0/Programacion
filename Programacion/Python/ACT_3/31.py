#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.

var1="A quién madruga Dios ayuda"
print(var1)
var2=input("Introduce la palabra:")
if var2 not in var1:
    print("La palabra no esta en la frase")
elif var2=="A":
    print("La palabra esta en la frase y esta en el i­ndice 1")
elif var2=="quién":
    print("La palabra esta en la frase y esta en el i­ndice 2")
elif var2=="madruga":
    print("La palabra esta en la frase y esta en el i­ndice 8")
elif var2=="Dios":
    print("La palabra esta en la frase y esta en el i­ndice 16")
elif var2=="ayuda":
    print("La palabra esta en la frase y esta en el indice 21")
