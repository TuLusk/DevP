maior=0
menor=0
for c in range(1, 8):
    idade=int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    idade=2022-idade
    if idade>=18:
        maior=maior+1
    elif idade<18:
        menor=menor+1
print('de todas as {} pessoas inseridas aqui, {} são maiores de idade e {} são menores'.format(c, maior, menor))
