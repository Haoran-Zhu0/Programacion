#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

var1=float(input("introduce tu nota:"))

if var1>10 or var1<0:
    print(f"La nota que has introducido no esta entre 0 y 10")  
elif var1>=8.5:
    print(f"has sacado un exelente")
elif var1>=6.5 and var1<8.5:
    print(f"has sacado un notable")
elif var1>=5 and var1<6.5:
    print(f"has sacado un satisfactorio")
elif var1<5:
    print(f"has sacado un insuficiente")