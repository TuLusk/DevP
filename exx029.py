velocidade = int(input('Qual a velocidade que você estava dirigindo: '))
if velocidade > 80:
    multa = velocidade-80
    preço = multa * 7
    print('Você ultrapassou o limite de velocidade por {}Km/h'.format(multa))
    print('Sua multa equivale a R${:.2f}'.format(preço))
else:
    print('Muito obrigado pelo seu tempo, tenha um bom dia!')
