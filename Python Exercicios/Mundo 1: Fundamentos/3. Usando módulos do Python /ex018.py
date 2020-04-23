'''
Faça um programa que leia um angulo qualquer e
mostra na tela o valor do seno. cosseno e tangente
desse triangulo
'''

from math import radians,cos, sin, tan

a = float(input("Digite um angulo emº "))
a = radians(a)

print('Cosseno do angulo {:.2f}\nSeno do angulo {:.2f}\nTangente do angulo {:.2f}'.format(cos(a), sin(a), tan(a)))
