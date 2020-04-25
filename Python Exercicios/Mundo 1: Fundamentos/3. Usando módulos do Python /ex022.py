"""
Crie um programa que leia o nome completo
de uma pessoa e mostre:
    o nome com todas as letras maiusculas
    o nome com todas minusculas
    quantas letras ao todo (sem considerar espaços)
    quantas letras tem o primeiro nome
"""

nome = input('Nome completo: ')

print('Em maisucula: {} letras.'.format(nome.upper()))
print('Em minuscula: {} letras.'.format(nome.lower()))
print('Tamanho do nome: {} letras.'.format(len(nome) - nome.count(' ')))

tam = nome.split()

print('Tamanho primeiro nome: {} letras.'.format(len(tam[0])))
