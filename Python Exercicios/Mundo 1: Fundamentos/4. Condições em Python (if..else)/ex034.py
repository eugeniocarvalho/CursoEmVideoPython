'''
Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento
Para salários superiores as 1.250, calule um aumento de 10%,
Para os inferiores ou iguais, o aumento é de 15%
'''

n = float(input('Salario: '))

if n > 1250:
    print('Novo salario: R$ {:.2f}'.format(n * 1.1))
else:
  print('Novo salario: R$ {:.2f}'.format(n * 1.15))

