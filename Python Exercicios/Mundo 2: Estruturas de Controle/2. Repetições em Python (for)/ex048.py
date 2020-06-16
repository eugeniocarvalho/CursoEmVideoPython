'''
Faça um programa que calcule a soma entre todos os numeros impares que sao
 multiplos de tres e que se encontram no intervalo de 1 ate 500
'''

cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += i

print('A soma de todos os impares divisiveis por 3 ate 500 é: {}'.format(cont))
