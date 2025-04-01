valorum=0
valordois=0
escolha=0
valorum = int(input('Digite o primeiro valor: '))
valordois = int(input('Digite o segundo valor: '))
while escolha != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    escolha=int(input(''))
    if escolha==1:
        print(valorum+valordois)
    elif escolha==2:
        print(valorum*valordois)
    elif escolha==3:
        if valorum>valordois:
            print('O maior valor é o {}'.format(valorum))
        elif valordois>valorum:
            print('O maior valor é {}'.format(valordois))
    elif escolha==4:
        valorum = int(input('Digite o primeiro valor: '))
        valordois = int(input('Digite o segundo valor: '))
print('Obrigado por usar')