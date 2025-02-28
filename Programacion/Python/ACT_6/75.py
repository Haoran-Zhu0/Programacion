#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

lista1=["a","b","D","x","r","X",3,"h","w",2,"i"]
var1=0
var2=0
var3=0
suma=0
for valor in lista1:
    if str(valor).isdigit():
        var1+=1
        suma+=int(valor)
    elif str(valor).isalpha():
        var2+=1
        if valor.isupper():
            var3+=1

total=len(lista1)

print(f"Número de valores:{total}")
print(f"Cantidad de números:{var1}")
print(f"Cantidad de letras:{var2}")
print(f"Cantidad de mayúsculas:{var3}")
print(f"Suma total de números:{suma}")
