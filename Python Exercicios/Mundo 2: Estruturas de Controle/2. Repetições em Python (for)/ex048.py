'''
Faça um programa que calcule a soma entre todos os numeros impares que sao
 multiplos de tres e que se encontram no intervalo de 1 ate 500
'''

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        print(i)
