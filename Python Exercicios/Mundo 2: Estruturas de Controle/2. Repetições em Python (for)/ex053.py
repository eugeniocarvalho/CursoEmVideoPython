'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
'''

temp = input().strip()

temp = temp.split(' ')

frase = ''.join(temp)

j = len(frase) - 1
i = 0

for i in range(len(frase)):
    if frase[i] == frase[j]:
        j -= 1
    else:
        break

if j < 0:
    print('É palindromo')
else:
    print('Não é palindromo')
