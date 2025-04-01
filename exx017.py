import math

oposto = float(input('Qual a medida do cateto oposto? :'))
adjacente = float(input('Qual a medida do cateto adjacente? :'))
opostoquadrado = oposto ** 2
adjacentequadrado = adjacente ** 2
hipotenusaquadrada = opostoquadrado + adjacentequadrado
hipotenusa = math.sqrt(hipotenusaquadrada)
print('A hipotenusa do triangulo retangulo em questão é {:.2f}'.format(hipotenusa))
