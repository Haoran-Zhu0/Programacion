#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

secreta=input("Introduce la palabra secreta:")
for contador in range(len(secreta)):
    letra=input("Introduce una letra:")
    
    for var in range(len(secreta)):
        
        if letra==secreta[var]:
            print(f"la letra se encuentra en la posición",var+1)
        
    if not letra in secreta:
        print("La letra no existe")