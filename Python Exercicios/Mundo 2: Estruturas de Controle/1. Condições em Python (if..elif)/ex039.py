'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''

from datetime import date

ano = int(input())
data = date.today().year

if data - ano < 18:
    print('Você ainda vai se alistar')
elif data - ano < 45:
    print('É hora de se alistar')
else:
    print('Passou do prazo')
