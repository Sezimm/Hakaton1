p = int(input("Vedite 4xznachnoe chislo: "))

a = p // 1000
b =	(p // 100)%10
c = (p//10)%10
d = p%10
v = [a,b,c,d]

c = list(reversed(sorted(v)))
if v == c:
	print("Yes")
else:
	print("No")