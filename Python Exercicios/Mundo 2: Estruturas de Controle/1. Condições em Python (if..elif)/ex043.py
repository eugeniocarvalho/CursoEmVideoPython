'''
desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:

- avaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 ate 30: sobrepeso
- 30 ate 40: obesidade
- acima de 40: obesidade móbida
'''

peso = float(input())
altura = float(input())

imc = peso / pow(altura, 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
