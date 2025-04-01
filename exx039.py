nascimento = int(input('Digite o ano de seu nascimento: '))
idade = 2021-nascimento
if idade < 18:
    faltando = 18 - idade
    print('Faltam ainda {} anos para o senhor se alistar meu jovem'.format(faltando))
elif idade == 18:
    print('O senhor está na idade exata para se alistar, se apresente imediatamente ao local de alistamento de sua '
          'cidade')
else:
    sobrando = idade - 18
    print('O senhor já passou da idade do alistamento militar por {} anos'.format(sobrando))
