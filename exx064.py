contador=0
soma=0
while True:
    numero=int(input('Digite um número(999 irá parar o programa): '))

    if numero==999:
        break

    contador += 1
    soma += numero

print('Foram digitados {} números'.format(contador))
print('E a soma entre eles é {}'.format(soma))
