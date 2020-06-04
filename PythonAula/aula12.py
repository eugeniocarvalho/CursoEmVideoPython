nome = str(input('Qual seu nome? '))

if nome == 'Eugênio':
    print('Belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')

print('Prazer em conhecê-lo {}'.format(nome))
