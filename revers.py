import sys
def dodo():
	a = input("Kak rab f rev: ")
	a = a.split(' ')
	v = ''.join(reversed(a[0]))
	print(v)

try:
	dodo()
		
except SyntaxError:
	dodo()
		