print('=-'*5,'Ano bissexto','-='*5)
ano=int(input('Digite o ano em que você está atualmente: '))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))