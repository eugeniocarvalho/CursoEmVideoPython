'''
Faça um programa que leia o nome completo de
uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
'''

nome = input('Nome completo:').strip()

nome = nome.split()

print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))

