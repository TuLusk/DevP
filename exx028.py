import random
print('=-'*5,'Jogo da adivinhação','-='*5)
print('A maquina escolheu um número entre 0 e 5, tente descobrir qual é')
sorte=random.randint(0,5)
jogador=int(input('sua resposta é: '))
if sorte==jogador:
    print('Meus Parabéns!!! Você adivinhou corretamente')
elif jogador >=6 or jogador<0:
    print('UEPA, PERA AI AMIGÃO, VOCÊ ESCOLHEU UM NÚMERO INVALIDO')
else:
    print('Mas que pena, você errou o número, mais sorte na proxima')
