var1=input("introduce una letra:")
l=var1.isupper()
n=var1.isnumeric()
m=var1.islower()
if n==True:
    print("El valor introducido es un numero")   
if m==True:
    print("Es minuscula")
if l==True:
    print("Es mayuscula")
elif l==False and n==False and m==False:
    print("El valor introducido es un simbolo")