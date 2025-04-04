a,b,a1,b1= map(int,input().split())

if a==a1 and b==b1:
    print("=")

elif a1<=a and b<=b1:
    print("1")

elif a<=a1 and b1<=b:
    print("2")

else:
    print("?")
