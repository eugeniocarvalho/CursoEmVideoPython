'''
Faça um programa qu leia um numero inteiro e diga se ele e ou nao numero primo
'''

num = int(input())
sum = 0

for i in range(1, num + 1):
    if num % i == 0:
        sum += 1
        print('\033[1;32m{}\033[0;0m'.format(i), end=' ')
    else:
        print('\033[1;31m{}\033[0;0m'.format(i), end= ' ')

print()
if sum <= 2:
    print('\033[1;94mÉ primo')
else:
    print('\033[033;91mNão é primo')
