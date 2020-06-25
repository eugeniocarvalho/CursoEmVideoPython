'''
Faça um programa que jogue par ou impar com o computdaor.
O jogo só sera interrrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randrange

num = 0

while True:
    player = int(input('Escolha um numero: '))
    pc = randrange(10)

    opcao = ' '
    print(f'Você jogou {player} e o computador jogou {pc}')

    while opcao not in 'PI':
        opcao = input('Par ou Impar? P/I: ').upper().split()[0]

    if opcao == 'P':
        if (player + pc) % 2 == 0:
            print('Voccê ganhou!!')
            num += 1
        else:
            print('Você perdeu :/')
            break

    if opcao == 'I':
        if (player + pc) % 2 != 0:
            print('Voccê ganhou!!')
            num += 1
        else:
            print('Você perdeu :/')
            break

print(f'Você ganhou {num} vezes conssecutivas')