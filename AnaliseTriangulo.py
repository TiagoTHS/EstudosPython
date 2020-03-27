print("---Digite os lados do Triangulo um de cada vez---")

a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))

#Verificação 
if a > (b + c) or b > (a + c) or c > (a + b):
	print("Nao e possivel formar triangulo")
else:
	#Perimetro
	per = a + b + c
	print(f"O perimetro do triangulo mede {per}")

	#Tipo 
	if a == b == c:
		print("O triangulo é equilatero")
	elif a==b or a==c or b==c:
		print("O triangulo é isoceles")
	else:
		print("O triangulo é escaleno")
	
	#Retangulo
	r = input("O triangulo possui um angulo de 90°? ").strip().upper()[0]
	if r == 'S' :
		print("Retangulo = True")
	else:
		print("Retangulo = False")
	
