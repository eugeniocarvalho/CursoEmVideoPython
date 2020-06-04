"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5 : reprovado
- média entre 5 e 6.9 : recuperação
- média 7 ou superior: aprovado
"""

nota1 = float(input(' '))
nota2 = float(input(' '))

media = (nota1 + nota2) / 2

if media < 5:
    print('reprovado! :(')
elif media < 7:
    print('Recuperação! :|')
else:
    print('Aprovado! :D')
