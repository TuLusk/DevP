frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso=''
for letra in range(len(junto)-1, -1, -1):
    inverso +=junto[letra]
if junto==inverso:
    print('Meus parabéns, {} é um palindromo'.format(frase))
else:
    print('Mas que pena, {} não é um palindromo'.format(frase))