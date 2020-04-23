'''
Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um triangulo
retangulo, calcule e mostre o comprimento da hipotenusa
'''

import math

cat_oposto = float(input('Cateto oposto: '))
cat_adj = float(input('Cateto adjacente: '))

hip = math.hypot(cat_oposto, cat_adj)

print('A hipotenusa tem tamanho: {:.2f}.'.format(hip))
