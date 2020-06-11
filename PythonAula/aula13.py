for i in range(5):
    print('{}'.format(i))

print('FIM')

for i in range(5, 0, -1):
    print('{}'.format(i))

print('FIM')

for i in range(0, 5, 2):
    print('{}'.format(i))

print('FIM')
print()

s = 0

for i in range(0, 4):
    n = int(input('Digite um valor '))
    s += n

print('O somatório é: {}'.format(s))
