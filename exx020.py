import random

nome1 = str(input('Qual é o nome do primeiro aluno? :'))
nome2 = str(input('Qual é o nome do segundo aluno? :'))
nome3 = str(input('Qual é o nome do terceiro aluno? :'))
nome4 = str(input('Qual é o nome do quarto aluno? :'))
nomes = [nome1, nome2, nome3, nome4]
random.shuffle(nomes)
print('A ordem de apresentação é a seguinte: {}'.format(nomes))
