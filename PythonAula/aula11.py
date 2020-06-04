print('\033[34mTexto\033[m')
print('\033[30;41mTexto\033[m')
print('\033[1;34;42mTexto\033[m')
print('\033[31;40mTexto\033[m')
print('\033[4;37mTexto')
print('\033[7;37;44mTexto\033[m\n')

nome = 'Eugênio'

print('Olá {}{}{}, prazer em te conhecer!!!'.format('\033[32m', nome, '\033[m'))

texto = 'Tres Pratos de Trigo para Tigres Tristes'
total = texto.upper().count(texto[0])
print(total)