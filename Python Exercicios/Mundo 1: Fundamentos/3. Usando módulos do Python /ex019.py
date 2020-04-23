'''
Um professor quer sortear um dos seus quatros alunos para
apagar o quadro. Faça um pograma que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido
'''

from random import randint

nome = input('Digite o nome dos alunos: ')

nome = nome.split(' ')
i = randint(1, 4)

print('Aluno escolhido foi: {}'.format(nome[i]))
