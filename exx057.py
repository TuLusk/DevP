male = female = 0
erro = 0
while erro == 0:
    resposta = str(input('Sexo do participante [M/F]: ')).upper()
    if resposta == 'F':
        female += 1
        erro += 1
    elif resposta == 'M':
        male += 1
        erro += 1
    else:
        erro = 0
        print('Tente novamente!')
print('Obrigado por participar!')