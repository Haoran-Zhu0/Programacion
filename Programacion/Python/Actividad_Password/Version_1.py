#Instruccion
print("La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters")
print("El posicion 1 tiene que ser,Un numero major o igual a 1 i menor o igual que 5")
print("El posicion 2 tiene que ser,Una lletra minuscula")
print("El posicion 3 tiene que ser,Una lletra mayuscula")
print("El posicion 4 tiene que ser,Un dels següents simbols:*,_,@")
print("El posicion 5 tiene que ser,Una lletra minuscula")
print("El posicion 6 tiene que ser,Un numero major o igual a 6 i menor o igual que 9")
print("El posicion 7 tiene que ser,Un dels següents simbols:&,/,#")
print("El posicion 8 tiene que ser,Un numero menor o igual que5")
#Input, sirve para que el usuario introduzca la contraseña
var1=input("Introduce la contraseña:")
#logitud=len del var1, es decir, len sirve para medir la longitud del variable
log=len(var1)
error=0
#Indica la longitud del password que tiene que tener una longitud de entre 6 y 8 caracteres
if log>8 or log<6:
    print(f"Error, el password té una longitud de {log} caràcters i no compleix els requisits")
#else=si no, es decir, si cumple el if anterio para la programa si no sigue el programa
else:
#if not=si el primer caracter no es <=1 y >=5, printea error y si esta bien sigue el programa   
    if not int(var1[0])<=1 and int(var1[0])>=5:
        print("Error en el caracter 1")
#Si da error en toces suma 1 error, es decir, para llegar al final de la programa no tiene
#que dar ninguna error(no sumar nada) y el error sera 0 y en final he puesto un error=0
#para si hay error no printea la contraseña es correcta, si no hay error entoces printea es correcto.
        error=error+1
#Si la segunda caracter de la contraseña no es minuscula(islower), entoces printea error
    if not(var1[1]).islower()==True:
        print("Error en el caracter 2")
        error=error+1
#isupper=mayuscula
    if not(var1[2]).isupper()==True:
        print("Error en el caracter 3")
        error=error+1
#Si en la quarta caracte no hay siguientes signos(*,_,@), printea error
    if (var1[3]) not in "*_@":
        print("Error en el caracter 4")
        error=error+1
    if not(var1[4]).islower():
        print("Error en el caracter 5")
        error=error+1
#Si en el caracter 6 el numero no es >=6 y <=9, printea error
    if not int(var1[5])>=6 and int(var1[5])<=9:
        print("Error en el caracter 6")
        error=error+1
#Si el logintud de la contraseña hay un valor en el caracter 7.
    elif log==7:
        if (var1[6]) not in "&/#":
            print("Error en el caracter 7")
            error=error+1
#Si el logintud de la contraseña hay un valor en el caracter 8.
    elif log==8:         
        if not int(var1[7])<=5:
            print("Error en el caracter 8")
            error=error+1
    if error==0:
        print("El format de la CONTRASEÑA es correcte")