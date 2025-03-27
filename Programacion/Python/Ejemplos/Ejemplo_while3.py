contador=0
longitud=0
var1=input("Introduce una contraseña:")
longitud=len(var1)
while longitud!=8:
    contador+=1
    print(contador)