var1=input("introduce una letra:")
l=var1.isupper()
n=var1.isnumeric()
m=var1.islower()
if m==True:
    print("Es minuscula")
if l==True:
    print("Es mayuscula")
if l==False and n==True:
    print("Es mayuscula¿?")