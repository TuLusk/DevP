print('-='*5,'WILL IT TRIANGLE','=-'*5)
r1=float(input('1° Medida: '))
r2=float(input('2° Medida: '))
r3=float(input('3° Medida: '))
triangulo=r1-r2<r3<r1+r3 and r1-r3<r2<r1+r3 and r3-r2<r1<r3+r2
if triangulo:
    print('É possível formar um triângulo com essas medidas')
else:
    print('É impossível formar um triângulo com essas medidas')
