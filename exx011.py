altura = float(input('Qual a altura da parede? :'))
largura = float(input('Qual a largura da parede? :'))
area = altura * largura
tinta = area / 2
print('A área de uma parede que tem {} metros de altura e {} metros de largura é {}, sabendo disso, é necesário {} litros de tinta'.format(altura, largura, area, tinta))
