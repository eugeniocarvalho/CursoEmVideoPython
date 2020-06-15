'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
- A media de idade do grupo
- QUal é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''

mediaIdade = 0
maiorIdade = 0
nomeMaisVelho = ''
cont = 0

for i in range(4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')
    print()

    mediaIdade += idade

    if sexo == 'f' or sexo == 'F':
        if idade < 20:
            cont += 1
    elif sexo == 'm' or sexo == 'M':
        if idade > maiorIdade:
            maiorIdade = idade
            nomeMaisVelho = nome

print('Média de idade: {}'.format(mediaIdade / 4))
print('Nome do homem mais velho: {}'.format(nomeMaisVelho))
print('Quantidade de mulher com menos de 20 anos: {}'.format(cont))
