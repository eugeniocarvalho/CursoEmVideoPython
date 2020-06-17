'''
Faça um programa que leia um numero qualquer e mostre o seu fatorial
'''

n = int(input())
fat = 1

print('Fatorial de {}'.format(n), end='')

while n > 1:
    fat *= n
    n -= 1

print(' = {}'.format(fat))
