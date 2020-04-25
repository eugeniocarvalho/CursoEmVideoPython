'''
Faça um programa que leia um numero de 0 a 9999
e mostre na tela cada um dos digitos separados

Ex: 1834

unidade:4
dezena:3
centena:8
milhar:1
'''

num = int(input('Número: '))

print('Analizando o numero: {}'.format(num))
print('unidade: {}'.format(num // 1 % 10))
print('dezena: {}'.format(num // 10 % 10))
print('centena: {}'.format(num // 100 % 10))
print('milhar: {}'.format(num // 1000 % 10))


