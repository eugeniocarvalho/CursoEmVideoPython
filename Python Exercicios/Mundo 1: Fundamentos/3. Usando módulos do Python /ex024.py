'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "Santo"
'''

cidade = input('Nome da cidade: ').strip()

r = 'santo' in cidade[:5].lower()

print(r)


