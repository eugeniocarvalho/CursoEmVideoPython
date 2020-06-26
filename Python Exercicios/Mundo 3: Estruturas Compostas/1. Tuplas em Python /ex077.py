'''
Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = (
'oi', 'mano', 'palestra', 'doom', 'cachorro', 'pao', 'abraço', 'farinha', 'chapisco', 'micalateia', 'abrobinha',
'macaco', 'paralalepipedo', 'firma', 'borracha', 'barbeador', 'caneca', 'chave')

for p in palavras:
    a = e = i = o = u = 0
    print(f'Palavra {p} tem', end=' ')
    for j in range(len(p)):
        if p[j] == 'a':
            a += 1
        if p[j] == 'e':
            e += 1
        if p[j] == 'i':
            i += 1
        if p[j] == 'o':
            o += 1
        if p[j] == 'U':
            u += 1
    print(f'{a+e+i+o+u} vogais')
