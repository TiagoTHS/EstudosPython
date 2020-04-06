from math import sqrt

def equacionar(a, b, c=0):
	delta = (b*b - 4*a*c)
	if delta >= 0:
		x1 = (-b + sqrt(delta))/(2*a)
		x2 = (-b - sqrt(delta))/(2*a)
		return x1, x2
	else:
		print("Nao existe raizes reais")
		
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("As raizes da equação são:", equacionar(a, b, c))
	