'''
Escreva um prograa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou entao o empréstimo será negado
'''

valCasa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
ano = int(input('Anos para pagar: '))

anoMeses = ano * 12
valorMes = valCasa / anoMeses

if (valorMes * 100) / salario < 30:
    print('Tudo ok para a compra')
else:
    print('O valor da prestação excedeu 30%')
