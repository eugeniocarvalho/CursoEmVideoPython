'''
Faça um algorimo que leia o salario de um funcionario
e mostre seu novo salario , com 15% de aumento
'''

salario = float(input('Qual é o salario do funcionário? '))

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, salario*1.15))
