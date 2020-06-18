'''
Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execição mostre media entre todos os valores e qual foi o maior e menor valor lido.
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
'''

cont = sum = 0
c = 1
maior = menor = 0
while c:
    n = int(input())
    if cont == 0:
        menor = n

    if n > maior:
        maior = n

    if n < menor:
        menor = menor

    cont += 1
    sum += n
    c = int(input())

print('Media: {}, maior: {}, menor: {}'.format(sum/cont, maior, menor))
