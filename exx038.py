print('=-'*5, 'COMPARADOR', '-='*5)
um = int(input('Digite o primeiro valor: '))
dois = int(input('Digite o segundo valor: '))

if um > dois:
    print('O primeiro valor é maior que o segundo valor')
elif um < dois:
    print('O segundo valor é maior que o primeiro')
elif um == dois:
    print('Os dois valores são iguais')
