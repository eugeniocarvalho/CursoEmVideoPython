'''
Faça um programa que mostre a tabuada de varios números,
um de cada vez, para cada valor digitado pelo usuario.
O programa sera interrmpido quando o numero solicitado for negativo
'''

while True:
    n = int(input())

    if n != 0:
        for i in range(11):
            print(f'{n} x {i} = {i * n}')
    else:
        break
    print()
