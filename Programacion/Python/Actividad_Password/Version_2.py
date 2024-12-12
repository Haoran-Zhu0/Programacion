print("La longitud del password debe ser entre 6 y 8 caracteres")
print("Debe contener, al menos 3 números del 1 al 9, 2 letras mayúsculas o minúsculas y 2 símbolos(*_@/&#)")
print("Un numero mayor o igual 1 y menor o igual 5")
print("Un numero mayor o igual 6 y menor o igual 9")
print("Debes introducir 3 contraseñas")
correctas=0
incorrectas=0
for contador in range(3):
    var1=input(f"Introduce la contraseña {contador+1}:")    
    if len(var1)<6 or len(var1)>8:
        print("Error: La contraseña debe tener entre 6 y 8 caracteres")
        incorrectas+=1
else:
    numeros=0
    letras_minusculas=0
    letras_mayusculas=0
    simbolos=0
    for x in var1:
        if not x.isnumeric:
            print("Debe tener 3 numeros del 1 al 9")
        elif x.isnumeric():
            numeros+=1
        if not x.isalpha():
            print("Debe tener dos letras(mayúsculas o minúsculas)")
        elif x.islower():
            letras_minusculas+=1
        elif x.isupper():
            letras_mayusculas+=1
        if not x in "*@/&#":
            print("Debe tener 2 simbolos(*@/&#)")
        elif x in "*_@/&#":
            simbolos+=1
        
    if numeros>=3 and letras_minusculas>=2 and letras_mayusculas>=1 and simbolos>=2:
        print("La contraseña es correcta")
        correctas+=1
    else:
        print("La contraseña no cumple con los requisitos")
        incorrectas+=1

print(f"Contraseñas correctas:{correctas}")
print(f"Contraseñas incorrectas:{incorrectas}")
