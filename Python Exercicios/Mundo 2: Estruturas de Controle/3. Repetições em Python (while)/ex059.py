'''
Crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
'''

n1 = int(input())
n2 = int(input())
n = 1

while n != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    ''')
    n = int(input())

    if n == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif n == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif n == 3:
        if n1 > n2:
            print('{} maior que {}'.format(n1, n2))
        else:
            print('{} maior que {}'.format(n2, n1))
    elif n == 4:
        n1 = int(input())
        n2 = int(input())
    else:
        print('Opção invalida, tente novamente')
