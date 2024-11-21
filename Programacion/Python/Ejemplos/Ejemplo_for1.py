#range(0,10)
#string
var=0
total=0

var_min=int(input("Introduce un valor minimo:"))
var_max=int(input("Introduce un calor maximo:"))

for contador in range(var_min,var_max):
    total=var+contador
print(total)