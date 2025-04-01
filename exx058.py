import random
print('=-'*5,'Jogo da adivinhação','-='*5)
print('A maquina escolheu um número entre 0 e 10, tente descobrir qual é')
sorte=random.randint(0,10)
tentativas=1
jogador=15
while jogador!= sorte:
    jogador = int(input('sua resposta é: '))
    if jogador!=sorte:
        print('Errado! Tente novamente')
        tentativas+=1
        if jogador>sorte:
            print('Um pouco menos')
        elif jogador<sorte:
            print('Um pouco mais')
print('Meus Parabéns! Você conseguiu!')
print('Foram necessárias {} tentativas'.format(tentativas))