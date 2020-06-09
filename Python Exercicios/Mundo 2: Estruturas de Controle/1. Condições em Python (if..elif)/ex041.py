
'''
A confederação nacional de notação precisa de um programa que leia o ano de nascimento
de um atleta e mostra sua categoria, de acordo com a idade:

- ate 9 anos: mirim
- ate 14 anos: infantil
- até 19 anos: junior
- até 25 anos: senior
- acima: master

'''

from datetime import date

ano = int(input())
data = date.today().year
ano = data - ano
if ano <= 0:
    print('Mirim')
elif ano <= 16:
    print('Infantil')
elif ano <= 19:
    print('Junior')
elif ano <= 25:
    print('Senior')
else:
    print('Master')

