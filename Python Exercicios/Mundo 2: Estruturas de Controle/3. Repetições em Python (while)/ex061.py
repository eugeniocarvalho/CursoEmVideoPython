'''
Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA,
 mostrando os 10 primeiros termos da progressao usando a estrutura while

 Desafio 51
    Desenvolva um programa que leia o primeiro termo e a razao de uma PA,
    No final, mostre os 10 primeiros termos dessa progressao

an = a1 + (n – 1)r
'''

a1 = int(input())
r = int(input())
i = 1
while i <= 10:
    print('{}'.format(a1 + (i - 1) * r), end=' ➔ ')
    i += 1

print('Acabou')