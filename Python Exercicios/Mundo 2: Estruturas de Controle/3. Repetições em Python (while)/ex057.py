'''
Faça um programa que leia o sexo de uma pessoa, mas so aceita os valore M ou F.
 caso esteja errado peça a digitação novamente ate tter um valor correto
'''

sexo = input()

while sexo != 'F' and sexo != 'M':
    print('Digite sexo novamente (M/F)')
    sexo = input()

