# As funções podem ser de dois tipo: Com ou sem Parametros
# Funções sem parametros são aquelas que não recebem nenhum valor para serem executadas
# Funções com parametros são aquelas que recebem valores para serem executadas

# Função sem parametros
'''
def somar():
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
somar()
'''
# Função com parametros
'''
def somar(n1, n2):
    return n1 + n2
print(somar(10, 20))
'''

# Também podemos dar dicas de tipos para os parametros

'''
def somar(n1: int, n2: int) -> int:
    return n1 + n2
print(somar(10, 20))
'''

# Além de também podermos criar um texto de documentação para a função
'''
def somar(n1: int, n2: int) -> int:
    """Função que soma dois números inteiros e retorna o resultado."""
    return n1 + n2
print(somar(10, 20))
print(somar.__doc__)
'''

# Também é possível criar funções com parametros padrões ou opcionais
'''
def somar(n1=0, n2=0):
    return n1 + n2
print(somar(10)) # Nesse caso o n2 vai assumir o valor padrão 0
print(somar()) # Nesse caso o n1 e o n2 vão assumir o valor padrão
'''

# Também é possível criar funções com um número indeterminado de parametros utilizando *

'''
def somar(*num):
    soma = 0
    for n in num:
        soma += n
    print(soma)
somar(1,2,3,4,5,6,7,8,9,10)
'''

