soma=0
contador=0
valores=[]
while True:
    valor=int(input('Digite um número inteiro: '))
    soma+=valor
    contador+=1
    valores.append(valor)
    continuar=str(input('Deseja continuar?(s/n): ').upper())
    if continuar=='N':
        break
media=soma/contador
maior=max(valores)
menor=min(valores)
print('A média dos valores é: {}'.format(media))
print('O maior valor é: {}'.format(maior))
print('O menos valor é: {}'.format(menor))