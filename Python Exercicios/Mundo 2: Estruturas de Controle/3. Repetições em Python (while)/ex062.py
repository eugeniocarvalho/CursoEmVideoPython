'''
Melhore o desafio 61, pesguntando para o usuario se ele quer mostrar mais alguns termos.
o programa encerra quando ele disser que quer mostrar 0 termos

 Desafio 61
     Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA,
     mostrando os 10 primeiros termos da progressao usando a estrutura while

         Desafio 51
            Desenvolva um programa que leia o primeiro termo e a razao de uma PA,
            No final, mostre os 10 primeiros termos dessa progressao

        an = a1 + (n – 1)r
'''

i = n = 1

while n != 0:
    a1 = int(input())
    r = int(input())
    print('{}'.format(a1 + (i - 1) * r), end=' ➔ ')
    i += 1
    n = int(input('Mostrar mais termos? '))

print('Acabou')
