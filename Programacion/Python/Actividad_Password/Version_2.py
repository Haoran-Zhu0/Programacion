print("La longitud del password debe ser entre 6 y 8 caracteres")
print("Debe contener 3 números, 2 letras y 2 símbolos")
print("Debe tener 2 minusculas y 1 mayuscula")
print("Dos numero mayor o igual 1 y menor o igual 5")
print("Un numero mayor o igual 6 y menor o igual 9")
print("Los simbolos deben de ser los siguiente:*_@/&#")
print("Debes introducir 3 contraseñas")
correctas=0
incorrectas=0
numeros=0
minusculas=0
mayusculas=0
simbolos=0
es_correcta=True
for contador in range(3):
    var1=input(f"Introduce la contraseña {contador+1}:")    
    if len(var1)<6 or len(var1)>8:
        print("Error: La contraseña debe tener entre 6 y 8 caracteres.")
        es_correcta=False
for x in var1:
    if x.isnumeric():
        if'1'<=x<='5':
            numeros+=1
    elif'6'<=x<='9':
        numeros+=1
    elif x.isalpha():
        if x.islower():
            minusculas+=1
    elif x.isupper():
        mayusculas+=1
    elif x in "*_@/&":
        simbolos+=1
    else:
        print("Error: La contraseña contiene caracteres no válidos.")
        es_correcta=False
        if es_correcta:
            if (numeros==3 and minusculas>=2 and mayusculas>=1 and simbolos>=2):
                print("La contraseña es correcta.")
                correctas+=1
else:
    print("La contraseña no cumple con los requisitos.")
    es_correcta=False
if not es_correcta:
    incorrectas+=1
print(f"Contraseñas correctas: {correctas}")
print(f"Contraseñas incorrectas: {incorrectas}")
