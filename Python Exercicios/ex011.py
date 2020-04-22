'''
Faça um programa que leia a largura e altura de uma parede
em metros, calcule a sua area e a quantidade de tinta necessario
para pinta-la, sabendo que cada litro de tinta, pinta a area de 2m²
'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

print('Sua parede tem a dimensão {}x{} e sua área é de {}m².'.format(largura, altura, largura*altura))
print('Para pintar sua parede você precisará de {}L de tinta.'.format((largura*altura)/2))
