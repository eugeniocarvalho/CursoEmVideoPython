'''
Crie um programa que leia varios numero inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999. que é a condição de parada.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
'''

n = int(input('Digite um numero [999] para sair: '))
sum = cont = 0

while n != 999:
    sum += n
    cont += 1
    n = int(input())

print('{} numeros digitados, e a soma deles é: {}'.format(cont, sum))
