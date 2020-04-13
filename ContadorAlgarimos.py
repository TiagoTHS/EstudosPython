def count_alg(num):
	num = str(num)
	for i in num:
		x.append(i)

n = int(input("Digite a quantidade de numeros que deseja analisar: "))

#lista x
x = []

for i in range(n):
	nro = input("Digite um numero: ")
	count_alg(nro)
					
#impressão dos resultados
print("0 -> ", x.count('0'))
print("1 -> ", x.count('1'))
print("2 -> ", x.count('2'))
print("3 -> ", x.count('3'))
print("4 -> ", x.count('4'))
print("5 -> ", x.count('5'))
print("6 -> ", x.count('6'))
print("7 -> ", x.count('7'))
print("8 -> ", x.count('8'))
print("9 -> ", x.count('9'))
