'''
Faça um programa que leia um número inteiro qualquer
 e mostre na tela sua tabuada
'''

n = int(input('Digite um numero para ver a tabuada: '))

print('------------')
for i in range(10):
    print('{} x {} = {}'.format(n, i+1, n*(i+1)))
print('------------')
