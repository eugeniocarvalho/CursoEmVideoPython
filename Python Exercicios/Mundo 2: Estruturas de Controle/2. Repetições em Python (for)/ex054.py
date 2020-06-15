'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores
'''

import datetime

atual = datetime.date.today().year
menor = 0
maior = 0

for i in range(7):
    ano = int(input())

    if atual - ano < 18:
        menor +=1
    else:
        maior +=1

print('Peesoas de menor: {}'.format(menor))
print('Pessoas de maior: {}'.format(maior))
