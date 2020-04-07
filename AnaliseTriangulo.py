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
	while True:
	        r = str(input("O triangulo possui um angulo de 90°?  [S/N]")).strip().upper()[0]
		if r in 'SN':
			if r == 'S':
				print("Retangulo = True")
			else:
				print("Retangulo = False")	
			break
		print("Escolha uma opcao valida!")
	
