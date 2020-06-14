'''
Desenvolva um programa que leia o primeiro termo e a razao de uma PA,
No final, mostre os 10 primeiros termos dessa progressao

an = a1 + (n – 1)r
'''

a1 = int(input())
r = int(input())

for i in range(1, 10):
    print(a1 + (i - 1) * r)
