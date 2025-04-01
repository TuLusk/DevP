print('=-'*5, 'Viagens','-='*5)
distancia=int(input('Digite a distância da sua viagem: '))
if distancia <= 200 and distancia > 0:
    valor= distancia*0.5
    print('O valor da sua viagem de {}Km equivale a R${:.2f}'.format(distancia,valor))
elif distancia > 200:
    valor= distancia*0.45
    print('O valor de sua viagem de {}Km equivale a R${:.2f}'.format(distancia,valor))
else:
    print('Sua viagem é invalida pois não é possível viajar para distâncias negativas')