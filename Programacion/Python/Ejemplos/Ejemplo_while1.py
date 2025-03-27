contador=1
par=0
impar=0
while contador<=20:
    if contador%2==0:
        print(f"{contador}es par")
        par+=1
    if contador%2!=0:
        print(f"{contador}es impar")
        impar+=1
    contador+=1