'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguntar se o usuario vai continuar. No final, mostre:

    A. qual é o total gasto na compra
    B. quantos produtos custam mais de 1000
    C. qual é o nome do produto mais barato
'''

total = qtd = menor = 0
barato = ''

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))

    if preco > 1000:
        qtd += 1

    if total == 0:
        menor = preco
        barato = nome

    total += preco

    if preco < menor:
        menor = preco
        barato = nome

    opção = input('Quer continuar? S/N ').upper()

    if opção != 'S':
        break

print(f'Total gasto de R$ {total:.2f}')
print(f'{qtd} produtos custam mais de R$ 1000,00')
print(f'O produto mais barato é {barato}, que custa {menor:.2f}')
