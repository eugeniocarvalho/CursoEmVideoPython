'''
Escreva um programa que leia um numero n inteiro qualquer e
mostre na tela os n primeiros elementos de uma sequencia de Fibonacci
'''

n = int(input())

a = f = i = 0
b = 1

while i < n:
    print(f, '→ ', end='')
    f = a + b
    b = a
    a = f
    i += 1

print('FIM')
