n = int(input("Digite a quantidade de numeros que deseja analisar: "))

#valor inicial zero para as variaveis contadoras
c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0

#lista x
x = []

#comando for para ler os numeros e adicionar a 'x'
for i in range(0, n):
	num = int(input("Digite um numero inteiro: "))
	nro = str(num)
	x.append(nro)

#comando for para realizar a contagem de cada algarismo 				
for c in range(0, n):
	c0 += x[c].count("0")
	c1 += x[c].count("1")
	c2 += x[c].count("2")
	c3 += x[c].count("3")
	c4 += x[c].count("4")
	c5 += x[c].count("5")
	c6 += x[c].count("6")
	c7 += x[c].count("7")
	c8 += x[c].count("8")
	c9 += x[c].count("9")
	
#impressão dos resultados
print("0 -> ", c0)
print("1 -> ", c1)
print("2 -> ", c2)
print("3 -> ", c3)
print("4 -> ", c4)
print("5 -> ", c5)
print("6 -> ", c6)
print("7 -> ", c7)
print("8 -> ", c8)
print("9 -> ", c9)

             


	

