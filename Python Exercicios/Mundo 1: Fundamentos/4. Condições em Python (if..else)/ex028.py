'''
Escreva um programa que faça o computador "pensar" em um
número int entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o número escolhido pelo computador

A saida é se o usuario ganhou ou perdeu
'''

import random
import time

pc = random.randrange(0, 5)
print('Estou pensando num número...')
time.sleep(2)

n = int(input('Que número eu pensei? de 0 a 5: '))

if n == pc:
    print('Ganhou!!')
else:
    print('Perdeu, pensei no número {}'.format(pc))
