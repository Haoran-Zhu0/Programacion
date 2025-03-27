var1=int(input())

if var1%400==0:
    print("YES")
elif var1%100==0:
    print("NO")
elif var1%4==0:
    print("YES")
else:
    print("NO")
