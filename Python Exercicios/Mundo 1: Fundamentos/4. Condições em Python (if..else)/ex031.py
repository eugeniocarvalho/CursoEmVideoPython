'''
Desenvolva um programa que pergunta a distancia de
uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 por km para viagens de até 200km e R$0,45 para
 viagens mais longas
'''

num = float(input())

if num <= 200:
    num *= 0.50
else:
    num *= 0.45

print('Preço da passagem R${:.2f}'.format(num))
