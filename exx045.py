import random
print('=-'*5, 'JOKENPO','-='*5)
print('[1] Tesoura'
      '[2] Papel'
      '[3] Pedra')
machine=random.randint(1,3)
player=int(input('Escolha sua opção: '))
if player==machine:
    print('Pelo visto você e a maquina empataram')
elif player==1 and machine==2:
    print('Pelo visto você venceu a maquina')
elif player==2 and machine==3:
    print('Pelo visto você venceu a maquina')
elif player==3 and machine==1:
    print('Pelo visto você venceu a maquina')
elif player==2 and machine==1:
    print('Pelo visto a maquina venceu você')
elif player==3 and machine==2:
    print('Pelo visto a maquina venceu você')
elif player==1 and machine==3:
    print('Pelo visto a maquina venceu você')
else:
    print('Você escolheu uma opção invalida!')