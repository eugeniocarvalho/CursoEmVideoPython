'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:3])
print()

for c in range(len(lanche)):
    print(f'Comendo {lanche[c]}, na posição {c}')

print()

for c in lanche:
    print(f'Comendo {c}')

print()

for pos, c in enumerate(lanche):
    print(f'Comendo {c}, na posição {pos}')

print('Muçei, to de buxin chei')

print()

print(sorted(lanche))
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(c.count(2))
print(c.index(8))

pessoa = ('Eugenio', 22, 'M', 65.50)
print(pessoa)
