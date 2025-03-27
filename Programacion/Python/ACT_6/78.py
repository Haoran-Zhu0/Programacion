#A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir.

lista=["a", "b", "D", "x", "r", "X", 3, "h", "w", 2, "i"]

while True:
    print("Lista actual:", lista)
    valor=input("Introduce el valor que deseas eliminar: ")
    
    if valor.isdigit():
        valor_num=int(valor)
        if valor_num in lista:
            lista.remove(valor_num)
            print(f"Se eliminó el número {valor_num}")
        else:
            print("El valor introducido no está en la lista")
    else:
        print("ERROR: Solo se pueden eliminar números")
    
    continuar=input("¿Deseas eliminar otro número? (s/n):").lower()
    if continuar!='s':
        break

print("\nLista final:", lista)
