'''
Crie uma trupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

    a. apenas os 5 primeiros colocados
    b. os ultimos 4 colocados da tabela
    c. uma lista com os times em ordem alfabetica
    d. em qual posição na tabela esta o time da chapecoense
'''

times = (
    'Botafogo', 'Corinthians', 'Flamengo', 'Fluminense', 'São Paulo', 'Coritiba', 'Atlético-MG', 'Athletico-PR',
    'Santos',
    'Palmeiras', 'Goiás', 'Vasco', 'Inter', 'Fortaleza', 'Bragantino', 'Grêmio', 'Sport', 'Bahia', 'Ceará',
    'Atlético-GO')

print(f'Os cinco primeiros: {times[:5]}')
print(f'Os ultimos 4 colocados: {times[-4:]}')
print(f'Lista em ordem Alfabetica: {sorted(times)}')

for p, c in enumerate(times):
    if c == 'Flamengo':
        pos = p
        break

print(f'Flamengo ta na {pos+1}ª posição')
