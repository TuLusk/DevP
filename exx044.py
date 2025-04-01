preçonormal=float(input('Digite o valor do item: '))
print('[1] a vista no Dinheiro/Cheque')
print('[2] a vista no cartão')
print('[3] 2 vezes no cartão')
print('[4] 3 vezes ou mais no cartão')
formadepagamento=int(input('Digite sua forma de pagamento: '))
if formadepagamento==1:
    porcentagem=preçonormal/100
    desconto=porcentagem*10
    preçofinal=preçonormal-desconto
    print('O preço final do seu item ficou em {} pois há um desconto de 10%!'.format(preçofinal))
elif formadepagamento==2:
    porcentagem=preçonormal/100
    desconto=porcentagem*5
    preçofinal=preçonormal-desconto
    print('O preço final do seu item ficou em {} pois há um desconto de 5%'.format(preçofinal))
elif formadepagamento==3:
    preçofinal=preçonormal/2
    print('O preço final do seu item ficou em {}, sendo {} por mês'.format(preçonormal, preçofinal))
elif formadepagamento==4:
    porcentagem=preçonormal/100
    juros=porcentagem*20
    preçofinal=preçonormal+juros
    mes=int(input('Quantos meses você vai pagar? '))
    preçomes=preçofinal/mes
    print('O preço final do seu iem ficou em {} pois há um jurus de 20%, sendo {} por mês'.format(preçofinal,preçomes))
