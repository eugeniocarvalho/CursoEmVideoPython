'''
Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = (
'oi', 'mano', 'palestra', 'doom', 'cachorro', 'pao', 'abraço', 'farinha', 'chapisco', 'micalateia', 'abrobinha',
'macaco', 'paralalepipedo', 'firma', 'borracha', 'barbeador', 'caneca', 'chave')

for p in palavras:
    print(f'\nPalavra {p.upper()} tem', end=' ')

    for j in p:
        if j.lower() in 'aeiou':
            print(j, end=' ')
