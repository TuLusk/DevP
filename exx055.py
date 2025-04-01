lista=[]
for c in range(1, 6):
    peso=int(input('Digite o peso da {} pessoa em números inteiros: '.format(c)))
    lista.append(peso)
    lista.sort()
print('Destas pessoas, a mais leve tem {} e a mais pesada {}'.format(lista[0], lista[4]))