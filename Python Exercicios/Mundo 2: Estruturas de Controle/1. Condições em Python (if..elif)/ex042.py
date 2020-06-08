'''
Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado

- equilatero: todos os lados iguais
- isosceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

a = float(input())
b = float(input())
c = float(input())

if abs(a - b) < c < a + b and abs(a - c) < b < a + c and abs(b - c) < a < b + c:
    print('\033[34mForma triangulo')

    if a == b and b == c:
        print('Triângulo Equilatero')
    elif a == b or a == c or b == c:
        print('Triangulo Isoceles')
    elif a != b and a != c and b != c:
        print('Triangulo Escaleno')
else:
    print('\033[31mNão forma triangulo')