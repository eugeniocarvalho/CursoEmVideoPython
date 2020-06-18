'''
Faça um programa que leia o sexo de uma pessoa, mas so aceita os valore M ou F.
 caso esteja errado peça a digitação novamente ate tter um valor correto
'''

sexo = str(input()).strip().upper()[0]

while sexo not in 'fFmM':
    print('Digite sexo novamente (M/F)')
    sexo = str(input()).strip().upper()[0]

print('Sexo {} registrado com sucesso!'.format(sexo))
