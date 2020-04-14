#Calculadora em que o usuário pode escolher a
quantidade de números que deseja realizar a operação.

def soma(list):
	s = 0
	for i in list:
		s += i
	return s


def sub(list):
	m = list[0]
	for i in list[1:]:
		m = m - i
	return m


def div(list):
	d = list[0]
	for i in list[1:]:
		d = d / i	
	return d


def mult(list):
	p = 1
	for i in list:
		p = p*i
	return p


print("-"*30)
print("{:30}".format("Calculadora Python"))
print("-"*30)
print()
print("1 - Somar")
print("2 - Subtrair")
print("3 - Dividir")
print("4 - Multipiclar")
print()
while True:
	r = int(input("Escolha uma operação: "))
	if r in [1, 2, 3, 4]:
		break
	print("Escolha uma opção válida!!")

li = []
q = int(input("Quantos numeros ira usar? "))
for i in range (q):
	n = int(input(f"{i+1}° Numero: "))
	li.append(n)
	
if r == 1:
	print("A soma é igual a", soma(li))

elif r == 2:
	print("A subtração é igual a", sub(li))
	
elif r == 3:
	print("A divisão é igual a", div(li))

else:
	print("A multiplicação é igual a", mult(li))
