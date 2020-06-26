'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
    a. quantas vezes apareceu o valor 9
    b. em que posição foi digitado o primeiro valor 3
    c. quais foram os numeros pares
'''

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

tupla = (n1, n2, n3, n4)

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 esta na {tupla.index(3) + 1}º posição')
print('Números pares: ', end='')

for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
