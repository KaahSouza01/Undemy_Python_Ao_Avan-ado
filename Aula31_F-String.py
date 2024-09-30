nome = 'karol'
altura = 1.60
peso = 53
imc = peso / altura ** 2
print(imc)

# formatação de String
# Colocando o 'f' habilita o texto de usar variaveis (chaves)
linha1 = f'{nome} tem {altura} de altura'
print(linha1)

# colocando o 'f' após um '.' e colocando um número. Ex:2. podemos escolher as casas decimais ex:.2f , .3f , .6f
linha2 = f'{nome} tem {altura:.5f} de altura'
print(linha2)

linha3 = f'Seu imc é {imc:.2f}'
print(linha3)
