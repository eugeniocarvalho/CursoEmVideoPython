'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar, descondere-o
'''

sum = 0

for i in range(6):
    num = int(input())

    if num % 2 == 0:
        sum += num

print('Soma dos numeros pares {}'.format(sum))
