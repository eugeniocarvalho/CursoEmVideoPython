'''
Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuario quer ou nao continuar. No final, mostre:

    A. quantas pessoas tem mais de 18 anos
    B. quantos homens foram cadastrados
    C. Quantas mulheres tem menos de 20 anos
'''

i = j = k = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: M/F ').upper()

    if idade >= 18:
        i += 1

    if sexo == 'M':
        j += 1

    if sexo == 'F' and idade < 20:
        k += 1

    opcao = input('Quer continuar? S/N ').upper()

    if opcao != 'S':
        break

print(f'Existem {i} pessoas maiores de 18 anos')
print(f'{j} homens foram cadastrados')
print(f'Existe {k} mulheres menores de 20 anos')
