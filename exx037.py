print('=-'*5, 'CONVERSÃO DE NÚMEROS', '-='*5)
n = int(input('Digite o número que você deseja converter: '))
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
o = int(input('Digite sua opção: '))
if o == 1:
    b = bin(n)
    print('O número {} é equivalente a {} em binario'.format(n, b))
elif o == 2:
    oc = oct(n)
    print('O número {} é equivalente a {} em octal'.format(n, oc))
elif o == 3:
    h = hex(n)
    print('O número {} é equivalente a {} em hexadecimal'.format(n, h))
else:
    print('Opção invalida!')
print('Tenha um bom dia!')
