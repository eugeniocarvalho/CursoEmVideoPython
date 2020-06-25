'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero int)
e o programa vai informr quantas cedulas de cada valor serao entregues

Obs: Considere que o caixa possui cedulas de 50, 20, 10 e 1
'''

sacar = int(input('Quantos você quer sacar? '))

a = b = c = d = 0

while sacar:
    a = sacar // 50
    sacar %= 50

    b = sacar // 20
    sacar %= 20

    c = sacar // 10
    sacar %= 10

    d = sacar // 1
    sacar %= 1

if a > 0:
    print(f'{a} notas de R$ 50,00')

if b > 0:
    print(f'{b} notas de R$ 20,00')

if c > 0:
    print(f'{c} notas de R$ 10,00')

if d > 0:
    print(f'{d} notas de R$ 1,00')
