def verificar_horizontal():
	for i in range (0, 9, 3):
		if (tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO):
			return True


def verificar_vertical():
	for i in range (3):
		if (tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO):
			return True


def verificar_diagonal():
	for i in [0, 2]:
		if (tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO):
			return True


def verificar_empate():
	if not VAZIO in tabuleiro:
		return True

#tabuleiro
VAZIO = " "
tabuleiro = [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO]

#jogadores
jogador1 = " "
jogador2 = " "

while True:
	jogador1 = input("Escolha X ou O: ").upper().strip()
	if jogador1 in 'XO':
		break
	print("Escolha uma opção valida!")

if jogador1 == 'X':
	jogador2 = 'O'
else:
	jogador2 = 'X'                                            

#indice
for i in range(0, 9, 3):
		print(i, "|", i+1, "|", i+2)

#o jogo            
jogavel = True
rodada = 0
vencedor = False

while jogavel:	
	rodada += 1
	casa  = int(input("Escolha uma casa: "))
	if tabuleiro[casa] == VAZIO:
		if rodada%2 == 1:
			tabuleiro[casa] = jogador1
		else:
			tabuleiro[casa] = jogador2
	else:
		rodada -= 1
		print("="*30)
		print("Escolha um lugar vazio!")
		print("="*30)
					
	for i in range(0, 9, 3):
		print(i, "|", i+1, "|", i+2, "       ", tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])	
	
#verificar horizontal
	if verificar_horizontal():
		vencedor = tabuleiro[casa]
		jogavel = False

#verificar vertical
	if verificar_vertical():
		vencedor = tabuleiro[casa]
		jogavel = False

#verificar diagonal
	if verificar_diagonal():
		vencedor = tabuleiro[casa]
		jogavel = False

#verificar empate
	if verificar_empate():
		jogavel = False
		print("Jogo empatado! DEU VELHA!")	
	
	if vencedor:
		print("Vencedor: ", vencedor)