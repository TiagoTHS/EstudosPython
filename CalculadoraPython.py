#Calculadora em que o usuário pode escolher a
#quantidade de números que deseja realizar a operação.

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
while True:
	n = int(input("Numero: "))
	li.append(n)
	if len(li) >= 2:	
		t = input("Deseja usar mais numeros?").upper().strip()[0]
		if t == "N":
			break
	
if r == 1:
	print("A soma é igual a", soma(li))

elif r == 2:
	print("A subtração é igual a", sub(li))
	
elif r == 3:
	print("A divisão é igual a", div(li))

else:
	print("A multiplicação é igual a", mult(li))
