a,b=map(int,input().split())

var1=a*100+b
billetes_500=var1//50000
var1%=50000
billetes_200=var1//20000
var1%=20000
billetes_100=var1//10000
var1%=10000
billetes_50=var1//5000
var1%=5000
billetes_20=var1//2000
var1%=2000
billetes_10=var1//1000
var1%=1000
billetes_5=var1//500
var1%=500
monedas_2=var1//200
var1%=200
monedas_1euro=var1//100
var1%=100
monedas_50=var1//50
var1%=50
monedas_20=var1//20
var1%=20
monedas_10=var1//10
var1%=10
monedas_5=var1//5
var1%=5
monedas_2c=var1//2
var1%=2
monedas_1c=var1//1
var1%=1

print(f"Banknotes of 500 euros: {billetes_500}")
print(f"Banknotes of 200 euros: {billetes_200}")
print(f"Banknotes of 100 euros: {billetes_100}")
print(f"Banknotes of 50 euros: {billetes_50}")
print(f"Banknotes of 20 euros: {billetes_20}")
print(f"Banknotes of 10 euros: {billetes_10}")
print(f"Banknotes of 5 euros: {billetes_5}")
print(f"Coins of 2 euros: {monedas_2}")
print(f"Coins of 1 euro: {monedas_1euro}")
print(f"Coins of 50 cents: {monedas_50}")
print(f"Coins of 20 cents: {monedas_20}")
print(f"Coins of 10 cents: {monedas_10}")
print(f"Coins of 5 cents: {monedas_5}")
print(f"Coins of 2 cents: {monedas_2c}")
print(f"Coins of 1 cent: {monedas_1c}")
