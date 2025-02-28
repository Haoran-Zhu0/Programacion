#Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.

milista=[]
var1=0
var1=int(input("Introduce las veces de numeros que quieres introduir:"))

for contador in range(0,var1):
    milista.append(int(input("Introduce un numero:"))) 
milista.sort()
print(milista)