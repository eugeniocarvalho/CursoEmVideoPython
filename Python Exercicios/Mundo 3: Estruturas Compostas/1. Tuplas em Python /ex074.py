'''
Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla

Depois disso, mostre a listagem e numeros gerados e tambem indique o menor e o maior valor que estao na tupla
'''

from random import randint

nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

maior = menor = nums[0]

for i in nums:
    if i > maior:
        maior = i

    if i < menor:
        menor = i

print(f'Números gerados: {nums}')
print(f'Maior {maior}')
print(f'Menor {menor}')
