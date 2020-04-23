'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada
'''

from random import shuffle

nome = input('Digite o nome dos alunos ')

nome = nome.split(' ')
shuffle(nome)

print('A ordem de aprensentação será\n{}'.format(nome))



