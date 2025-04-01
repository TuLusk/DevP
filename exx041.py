idade = int(input('Digite sua idade: '))
print('De acordo com sua idade')
if idade < 10:
    print('Sua classificação é: Mirim')
elif 9 < idade < 15:
    print('Sua classificação é: Infantil')
elif 14 < idade < 20:
    print('Sua classificação é: Junior')
elif idade == 20:
    print('Sua classificação é: Sênior')
else:
    print('Sua classificação é: Mestre')
