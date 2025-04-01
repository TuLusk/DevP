print('=-'*5,'Aumento','-='*5)
salario=float(input('Digite seu salário: '))
if salario>=1250.00:
    porcentagem=salario/100
    aumento=porcentagem*10
    salarionovo=salario+aumento
    print('Meus parabéns, você recebeu um aumento de 10%, deixando seu salário em R${:.2f}'.format(salarionovo))
else:
    porcentagem=salario/100
    aumento=porcentagem*15
    salarionovo=salario+aumento
    print('Meus parabéns, você recebeu um aumento de 15%, deixando seu salário em R${:.2f}'.format(salarionovo))
90