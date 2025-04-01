s=0
for c in range (3, 501, 3):
    if (c%2)==1:
        s=s+c
print('A soma entre todos os números ímpares múltiplos de 3 entre 1 e 500 são {}'.format(s))