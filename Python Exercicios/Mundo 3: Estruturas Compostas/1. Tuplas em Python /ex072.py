'''
Crie um prgrama que tenha uma trupla totalmente preenchida com uma contagem por extensão, de zero ate vinte.

Seu programa devera ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenção
'''

numeros = (
'zero', 'um', 'dois', 'trẽs', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'cartoze', 'quinze', 'dezessseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero [0:20]: '))

    while n < 0 or n > 20:
        n = int(input('Digite um numero [0:20]: '))

    print(f'Você digitou o numero {numeros[n]}')

    i = input('Quer continuar? S/N').strip().upper()[0]

    while i not in 'SN':
        i = input('Quer continuar? S/N ').strip().upper()[0]

    if i == 'N':
        break

