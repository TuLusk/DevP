dias = int(input('Por quantos dias você alugou o carro? :'))
kilometros = int(input('Quantos kilometros você rodou com o carro? :'))
preçodias = dias * 60
preçokm = kilometros * 0.15
preçototal = preçokm + preçodias
print('O preço total a pagar é de R${}'.format(preçototal))
