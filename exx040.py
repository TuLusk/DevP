pn = float(input('Digite sua primeira nota: '))
sn = float(input('Digite sua segunda nota: '))
soma = pn+sn
media = soma/2
if media < 5:
    print('Você foi reprovado!')
elif media >= 5 and media < 7:
    print('Você está de recuperação!')
else:
    print('Você passou de ano')
print('Sua nota foi {}'.format(media))
