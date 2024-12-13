print("La longitud del password debe ser entre 6 y 8 caracteres")
print("Debe contener 3 números, 2 letras y 2 símbolos")
print("Debe tener 2 minúsculas y 1 mayúscula")
print("Dos números mayores o iguales a 1 y menores o iguales a 5")
print("Un número mayor o igual a 6 y menor o igual a 9")
print("Los símbolos deben de ser los siguientes: *_@/&#")
print("Debes introducir 3 contraseñas")
correctas=0
incorrectas=0
for contador in range(3):
    var1=input(f"Introduce la contraseña {contador+1}:")
    numeros=0
    minusculas=0
    mayusculas=0
    simbolos=0
    es_correcta=True
    if len(var1)<6 or len(var1)>8:
        print("La contraseña debe tener entre 6 y 8 caracteres.")
        es_correcta=False

    for x in var1:
        if x.isnumeric():
            if '1'<=x<='5':
                numeros+=1
            elif '6'<=x<='9':
                numeros+=1
        elif x.isalpha():
            if x.islower():
                minusculas+=1
            elif x.isupper():
                mayusculas+=1
        elif x in "*_@/&#":
            simbolos+=1
        else:
            print(f"El carácter '{x}' no es válido.")
            es_correcta=False
    if numeros<3:
        print("La contraseña debe contener al menos 3 números.")
        es_correcta=False
    if minusculas<2:
        print("La contraseña debe contener al menos 2 letras minúsculas.")
        es_correcta=False
    if mayusculas<1:
        print("La contraseña debe contener al menos 1 letra mayúscula.")
        es_correcta=False
    if simbolos<2:
        print("La contraseña debe contener al menos 2 símbolos(*_@/&#).")
        es_correcta=False
    if es_correcta:
        print("La contraseña es correcta.")
        correctas+=1
    else:
        print("La contraseña no cumple con los requisitos.")
        incorrectas+=1
print(f"Contraseñas correctas:{correctas}")
print(f"Contraseñas incorrectas:{incorrectas}")
