frase = 'Curso em Video Python'

print(frase[3])
print(frase[9:14])
print(frase[:14])
print(frase[15:])
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.""")
print(frase.count('o'))
print(len(frase))

frase = '    Curso em Video Python  '

print(frase)
print(len(frase))
frase = frase.strip()
print(frase)
print(len(frase))
print('Curso' in frase)
print(frase.find('Video'))

div = frase.split()

print(div[0])
