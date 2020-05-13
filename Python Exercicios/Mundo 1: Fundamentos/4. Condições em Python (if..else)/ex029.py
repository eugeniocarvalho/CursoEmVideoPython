'''
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensasgem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada
km acima do limite
'''

v = float(input('Velocidade: '))

if v > 80:
    v = (v - 80) * 7
    print('Você foi multado por excesso de velocidade com o valor de R${:.2f}'.format(v))
