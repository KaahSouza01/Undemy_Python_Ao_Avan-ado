"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] - i = Inicio, f = Fim, p = Passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá Mundo'
print(variavel[-4])
print(variavel[5])

print(variavel[4:]) # do 4 em diantes ":"
print(variavel[4:6]) # do 4 ao 6, ele le até o 5 pois o 6 ele não lê 
                    # para ler o 6 teria que colocar um número a mais
print(variavel[4:7])
print(variavel[0:9:2]) # 0 = inicio, 9 = final, 2 = passos, casas que ele vai pegar(pega um e pula outro)
print(variavel[ : : -1])

print(len(variavel)) #conta caracteres