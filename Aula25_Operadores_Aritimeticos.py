'''
divisao = 10 / 2.2
print('Divisão', divisao)

divisao_inteira = 10 // 2.2
print('Divisão inteira', divisao_inteira)

exponenciacao = 10 ** 2
print('Exponenciação', exponenciacao)

modulo = 55 % 2 #resto da divisão
print("Módulo", modulo)

print(10 % 8 == 0)
'''

n1 = int(input('Número o qual quer dividir: '))
n2 = int(input('Dividendo: '))
print("O número", n1, "é divisivel pelo número",n2, "?",n1 % n2 == 0)