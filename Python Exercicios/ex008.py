'''
Escreva um programa que leia um valor em metros e o
exiba convertido em centimetros e milimetros
'''

x = float(input('Uma distância em metros: '))

print('{:3.3f}km\n{:3.2f}hm\n{:3.1f}dam\n{:2.0f}dm\n{:3.0f}cm\n{:3.0f}mm'.format((x/1000), (x/100), (x/10), (x*10), (x*100), (x*1000)))

