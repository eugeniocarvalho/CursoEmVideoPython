'''
Faça um programa qu leia um numero inteiro e diga se ele e ou nao numero primo
'''

num = int(input())
sum = 0

for i in range(1, num + 1):
    if num % i == 0:
        sum += 1

if sum <= 2:
    print('É primo')
else:
    print('Não é primo')
