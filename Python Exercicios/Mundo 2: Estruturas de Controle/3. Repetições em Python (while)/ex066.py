'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles
'''

sum = total = 0

while True:
    n = int(input())

    if n == 999:
        break

    sum += n
    total += 1

print(f'Total de {total} números e o somatório é: {sum}')
