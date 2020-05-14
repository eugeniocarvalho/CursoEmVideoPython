'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''

n = int(input())
maior = n
menor = n

n = int(input())

if n > maior:
    maior = n

if n < menor:
    menor = n

n = int(input())

if n > maior:
    maior = n

if n < menor:
    menor = n


print('Menor: {}\nMaior: {}'.format(menor, maior))
