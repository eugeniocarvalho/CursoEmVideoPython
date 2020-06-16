'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
'''

maior = 0
menor = 0

for i in range(5):
    peso = float(input())

    if menor == 0:
        menor = peso

    if peso >= maior:
        maior = peso

    if peso < menor:
        menor = peso

print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))
