'''
Faça um programa que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto
'''

n = float(input('Qual é o preço do produto? '))

print('O produto que custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}'.format(n, n*0.95))
