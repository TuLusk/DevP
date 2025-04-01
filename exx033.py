print('=-'*5,'Qual é maior','-='*5)
n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
lista=[n1,n2,n3]
listacerta=sorted(lista)
primeiro=listacerta[2]
ultimo=listacerta[0]
print('O maior número dentre os três é {}'.format(primeiro))
print('O menor número dentre os três é {}'.format(ultimo))