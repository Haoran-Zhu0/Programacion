#Introduccion
print("El password debe ser entre 6 y 8 caracteres")
print("El password debe tener 2 letras minúsculas y 1 letra mayúscula")
print("El password debe tener dos números mayores o iguales a 1 y menores o iguales a 5 y un número mayor o igual a 6 y menor o igual a 9")
print("El password debe tener 2 símbolos que deben de ser los siguientes: *_@/&#")
print("Debes introducir 3 contraseñas")
#Inicializar las variables
correctas=0
incorrectas=0
#El bucle se repite tres veces pidiendo tres contraseñas al usuario.
for contador in range(3):
    var1=input(f"Introduce la contraseña {contador+1}:")
    minusculas=0
    mayusculas=0
    numeros_bajos=0
    numeros_altos=0
    simbolos=0
    es_correcta=True
    # Obtiene la longitud de la contraseña.
    log=len(var1)
    # Verifica que la longitud de la contraseña esté entre 6 y 8 caracteres.
    if not log>8 or log<6:
        print("La contraseña debe tener entre 6 y 8 caracteres.")
        es_correcta=False
    # Recorre cada caracter de la contraseña y verifica las condiciones.
    for x in var1:
        if x.isnumeric():
            #Si el carácter es un número entre 1 y 5, pues se cuenta.
            if '1'<=x<='5':
                numeros_bajos+=1
            #Si el carácter es un número entre 6 y 9, pues se cuenta.
            elif '6'<=x<='9':
                numeros_altos+=1
        elif x.islower():
            minusculas+=1
        elif x.isupper():
            mayusculas+=1
        elif x in "*_@/&#":
            simbolos+=1
    #Verifica si la contraseña cumple con los requisitos de números.
    if numeros_bajos<2:
        print("La contraseña debe tener al menos 2 números entre 1 y 5.")
        es_correcta=False
    #Verifica si la contraseña tiene al menos 1 número entre 6 y 9
    if numeros_altos<1:
        print("La contraseña debe tener al menos 1 número entre 6 y 9.")
        es_correcta=False
    #Verifica si la contraseña tiene al menos 2 letras minúsculas.
    if minusculas<2:
        print("La contraseña debe contener al menos 2 letras minúsculas.")
        es_correcta=False
    #Verifica si la contraseña tiene al menos 1 letra mayúscula.
    if mayusculas<1:
        print("La contraseña debe contener al menos 1 letra mayúscula.")
        es_correcta=False
    #Verifica si la contraseña tiene al menos 2 símbolos válidos.
    if simbolos<2:
        print("La contraseña debe contener al menos 2 símbolos (*_@/&#).")
        es_correcta=False
     #Si todos los requisitos se cumplen la contraseña es correcta.
    if es_correcta:
        print("La contraseña es correcta.")
        correctas+=1
    else:
        print("La contraseña no cumple con los requisitos.")
        incorrectas+=1
#Muestra el número de contraseñas correctas e incorrectas.
print(f"Contraseñas correctas:{correctas}")
print(f"Contraseñas incorrectas:{incorrectas}")
