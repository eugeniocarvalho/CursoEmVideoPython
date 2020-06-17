c = 1

while c < 10:
    print(c)
    c += 1

print('Fim')

s = 's'

while s == 's':
    n = int(input('Digite um numero: '))
    s = input('Quer continuar? S/N').upper()

print('Fim')

p = i = 0
n = 1


while n:
    n = int(input('Digite um numero: '))

    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1

print('{} numero pares e {} numeros impares'.format(p, i))
