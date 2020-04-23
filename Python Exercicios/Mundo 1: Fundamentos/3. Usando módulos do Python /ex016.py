'''
Crie um programa que leia um número real qualquer
pelo teclado e mostra na tela a sua ṕorção inteira
'''

import math

num = float(input('Digite um número'))

r = math.modf(num)

print('O numero digitado foi {} e sua porçao inteira é {:.0f}'.format(num, r[1]))
