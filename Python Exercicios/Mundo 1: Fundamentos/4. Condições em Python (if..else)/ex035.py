'''
Faça um progeama que leia o comprimento de tres retas e
diga ao usuario se elas podem ou não formar um triangulo

Para construir um triângulo é necessário que a medida de
qualquer um dos lados seja menor que a soma das medidas
dos outros dois e maior que o valor absoluto da diferença
entre essas medidas
'''

a = float(input())
b = float(input())
c = float(input())

if abs(a - b) < c < a + b and abs(a - c) < b < a + c and abs(b - c) < a < b + c:
    print('\033[34mForma triangulo')
else:
    print('\033[31mNão forma triangulo')
