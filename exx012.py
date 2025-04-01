preço = float(input('Qual é o preço do item? :'))
desconto = (preço / 100) * 5
preço2 = preço - desconto
print('O preço de do item normalmente é R${}, porém, estamos com uma promoção de 5%, fazendo o preço ir para R${}'.format(preço, preço2))
