from random import randint
from time import sleep

def verificar_jogo():
	vencedor = False
	VAZIO = " "
#verificar horizontal	
	for i in range (0, 9, 3):
		if (tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO):
			vencedor = tabuleiro[i]
	
#verificar vertical
	for i in range (3):
		if (tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO):
			vencedor = tabuleiro[i]
	
#verificar diagonal
	for i in [0, 2]:
		if (tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO):
			vencedor = tabuleiro[i]
	
#verificar empate
	if not VAZIO in tabuleiro and vencedor == False:
		jogavel = False
		print("Jogo empatado! DEU VELHA!")
		return True	
		
	if vencedor:
		jogavel = False
		print("Vencedor: ", vencedor)
		return True


def mostrar_tabuleiro():
	for i in range(0, 9, 3):
		print(i, "|", i+1, "|", i+2, "       ", tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])

def casa_invalida():
	print("="*30)
	print("Escolha um lugar vazio!")
	print("="*30)

####Funcao contra o PC####
def contra_pc():
	rodada = 0
	jogavel = True
	vencedor = False
	while jogavel:	
		rodada += 1
		if rodada%2 == 1:
			print("__{Sua vez!}__")
			casa  = int(input("Escolha a casa: "))
			if tabuleiro[casa] == VAZIO:
				tabuleiro[casa] = jogador1
			else:
				rodada -= 1
				casa_invalida()
		else:
			print("__{Minha vez!}__")
			print("Deixe-me ver...")
			sleep(1.5)
			casa = randint(0,8)
			if tabuleiro[casa] == VAZIO:
				tabuleiro[casa] = jogador2
			else:
				rodada -= 1
				casa_invalida()
		
		mostrar_tabuleiro()
		if verificar_jogo():
			jogavel = False

####Funcao contra amigo####
def contra_amigo():
	rodada = 0
	jogavel = True
	vencedor = False
	while jogavel:	
		rodada += 1
		if rodada%2 == 1:
			print("Vez de ", jogador1)
			casa  = int(input("Escolha a casa: "))
			if tabuleiro[casa] == VAZIO:
				tabuleiro[casa] = jogador1
			else:
				rodada -= 1
				casa_invalida()
		else:
			print("Vez de ", jogador2)
			casa  = int(input("Escolha a casa: "))
			if tabuleiro[casa] == VAZIO:
				tabuleiro[casa] = jogador2
			else:
				rodada -= 1
				casa_invalida()
		
		mostrar_tabuleiro()
		if verificar_jogo():
			jogavel = False


##################
##### O JOGO #######
#################

#tabuleiro
VAZIO = " "
tabuleiro = [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO]

#jogadores
jogador1 = " "
jogador2 = " "

print("Escolha seu adversário [1/2]\n[1]. PC\n[2].Amigo")
while True:	
	adv = int(input())
	if adv == 1 or adv == 2:
		break
	print("Escolha uma opção valida!")

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
mostrar_tabuleiro()
        
if adv == 1:
	contra_pc()

else:
	contra_amigo()
	
	
