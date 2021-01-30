import math

a = int(input("Vedite 1oe chislo: "))
z = input("Vedite znack: ")
b = int(input("Vedite 2oe chislo: "))

if z == "+":
	print(a+b)
if z == "-":
	print(a-b)
if z == "*":
	print(a*b)
if z == "/":
	if b == 0:
		print("Na 0 delit nelzya!!!")
	else:
		print(a/b)

