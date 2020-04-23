'''
Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado
'''

q = int(input('Quantidade de dias alugados? '))
km = float(input('Quantos km percorridos? '))

r = (0.15 * km) + (q * 60)

print('O total a pagar é R${:.2f}'.format(r))

