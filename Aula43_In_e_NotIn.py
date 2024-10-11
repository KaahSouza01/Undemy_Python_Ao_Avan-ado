#in = entre , Not In = Não entre
# Strings são oteráveis

# 0 1 2 3 4 5
# o t a v i o
# 6 5 4 3 2 1

nome = 'otavio'
print(nome[2]) # Terceira casa, lembrando que conta com o '0' por isso a terceira

print('a' in nome) 
print('z' in nome)
# checa para ver se o 'a' está entre o nome 
print(10 * '-')

print('vio' not in nome)

nome = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')