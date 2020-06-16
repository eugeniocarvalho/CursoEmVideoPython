'''
Refaça o desafio 9, mostrando a tabuada de um número que o usuario escolher, so que agora utilizando for

DESAFIO 9:
    Faça um programa que leia um número inteiro qualquer
    e mostre na tela sua tabuada
'''

n = int(input(''))

for i in range(10):
    print('{} x {} = {}'.format(n, i + 1, n * (i+1)))
