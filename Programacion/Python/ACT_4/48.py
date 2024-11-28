#Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.

secreta=input("Introduce la palabra secreta:")
longitud=len(secreta)
for contador in range(longitud):
    letra=input("Introduce una letra:")
    
    if letra in secreta:
        print("La letra existe")
    else:
        print("La letra no existe")