'''
Melhore o jogo do desafio 28 onde o computador vai pesar em um numero entre 0 e 10.
So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer

    Desafio 28
        Escreva um programa que faça o computador "pensar" em um
        número int entre 0 e 5 e peça para o usuario tentar descobrir
        qual foi o número escolhido pelo computador

        A saida é se o usuario ganhou ou perdeu

'''

import random
import time

pc = random.randrange(0, 10)
print('Estou pensando num número...')
time.sleep(2)

n = int(input('Que número eu pensei? de 0 a 10: '))
num = 1
while n != pc:
    print('Não foi esse. ', end='')
    num += 1
    n = int(input('Que número eu pensei? de 0 a 10: '))

print('Acertou!!')
print('Numero de tentativas: {}'.format(num))
