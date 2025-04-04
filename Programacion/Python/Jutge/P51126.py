a,b,a1,b1=map(int,input().split())

var1=max(a, a1)
var2=min(b, b1)

if var1<=var2:
    print(f"[{var1},{var2}]")
else:
    print("[]")
