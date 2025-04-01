import colorsys
print('=-'*5, 'BANCO DO BRASIL', '-='*5)
salario = int(input('Digite o seu salário:'))
casa = int(input('Digite o valor do objeto que você deseja comprar: '))
ano = int(input('Digite em quantos anos você planeja pagar o emprestimo: '))
salario1porcento = salario / 100
salario30porcento = salario1porcento * 30
mes = ano * 12
valor = casa / mes
if valor >= salario30porcento:
    print('Infelizmente seu empréstimo foi negado')
else:
    print('Meus parabéns, seu empréstimo foi aprovado. Você estará pagando um total de R${:.2f} por mês pelos proxímos {} meses'.format(valor, mes))
