'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binario
-2 para octal
-3 para hexadecimal
'''

num = int(input('Numero para conversao: '))

print("""
1. Converter para binário
2. Converter para octal
3. Converter para Hexadecimal
""")
conversao = int(input())

if conversao == 1:
    print('{} convertido para binário: {}'.format(num, bin(num)))
elif conversao == 2:
    print('{} convertido para octal: {}'.format(num, oct(num)))
elif conversao == 3:
    print('{} convertido para hexadecimal: {}'.format(num, hex(num)))
