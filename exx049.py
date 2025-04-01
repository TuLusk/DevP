print('-='*5, 'Tabuada 2.0', '=-'*5)
n=int(input('Escolha o número que irá sair na tabuada: '))
for c in range (1, 11):
    m=n*c
    print('{} X {} = {}'.format(n,c,m))
print('-='*5,'FIM','=-'*5)