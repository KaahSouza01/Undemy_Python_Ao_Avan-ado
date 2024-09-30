a = 'a'
b = 'b'
c = 1.1

# cada chave '{}' refere a um valor na ordem da String A B C
string = 'a={} b={} c={}'

# ordem 1, 2, 3
formato = string.format(a, b, c)

#também posso juntar a string e o formato em um só
#Ex1:
formato2 = 'a={} b={} c={}'.format(a, b, c)
#Ex:2
string3 = 'a={} b={} c={:.3f}'
formato3 = string3.format(a, b, c)

# Caso queira formatar com casas decimais
# string = 'a={} b={} c={:.5f}'
#OBS: IndexError out of range significa que tem algum {} vazio, não foi declarado 

# Parametro nomeado é quando damos nome dentro das funções
#string4 = a={1} b={0} c={0}

string4 = 'a={nome1} b={nome2} c={nome3:.2f}'
formato4 = string4.format(
    nome1 = a,
    nome2 = b,
    nome3 = c
    #se um for nomeado, todos terão que ser também e por a ','
)


print(formato)
print(formato2)
print(formato3)
print(formato4)