'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar, descondere-o
'''

sum = 0
cont = 0
for i in range(6):
    num = int(input())

    if num % 2 == 0:
        sum += num
        cont += 1

print('Soma de {} numeros pares: {}'.format(cont, sum))
