'''
Faça um programa que leia uma frase pelo teclado
e mostre:
    Quantas vezes aparece a letra 'a'
    em que posição ela aparece a primeira vez
    Em que posição ela aparece a ultima vez
'''

frase = input('Frase: ').lower().strip()

print(frase.count('a'))
print('Aparece primeira vez em {}'.format(frase.find('a')))
print('Aparece ultima vez em {}'.format(frase.rfind('a')))

