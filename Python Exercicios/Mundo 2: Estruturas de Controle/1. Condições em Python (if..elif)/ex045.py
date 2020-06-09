'''
Crie um programa que faça o computador jogar o jokenpo com você
'''
import random

print("""
1. Pedra
2. Papel
3. Tesoura
""")
player = int(input())

pc = random.randrange(3)

if player == pc:
    print('Empate')
elif player == 1 and pc == 2:
    print('Escolhi papel. Perdeu!')
elif player == 1 and pc == 3:
    print('Escolhi Tesoura. Você Ganhou!')
elif player == 2 and pc == 1:
    print('Escolhi Pedra. Voccê Ganhou!')
elif player == 2 and pc == 3:
    print('Escolhi tesoura. Perdeu!')
elif player == 3 and pc == 1:
    print('Escolhi pedra. Perdeu!')
elif player == 3 and pc == 2:
    print('Escolhi papel. Você Ganhou!')


