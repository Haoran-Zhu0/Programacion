milista=[]
total=0

numero=int(input("Introduce un numero:"))

while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro un numero:"))
    
print(max(milista))
print(min(milista))

for recorrer in milista:
    total=total+recorrer
print(total)

