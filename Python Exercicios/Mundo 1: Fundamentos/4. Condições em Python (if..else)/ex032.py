'''
Faça um programa que leia um ano qualquer e mostra se ele é bissexto
'''

ano = int(input())
s = str(ano)

if (ano // 1 % 10 == 0) and (ano // 10 % 10 == 0):
    if ano % 400 == 0:
        print('{} é ano bissexto'.format(ano))
    else:
        print('{} não é ano bissexto'.format(ano))

else:
    if ano % 4 == 0:
        print('{} é ano bissexto'.format(ano))
    else:
        print('{} não é ano bissexto'.format(ano))
