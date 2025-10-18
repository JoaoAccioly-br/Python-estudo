# Criação de Funções e Varíaveis para o main.py

Senha = 1234
Email = 'joao@gmail.com'

def saudações(nome):
    return f'Olá, {nome}! Seja bem-vindo(a)!'
def soma(a, b):
    return a + b
def subtração(a, b):
    return a - b
def multiplicação(a, b):
    return a * b
def divisão(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro: Divisão por zero não é permitida.'
def potência(a, b):
    return a ** b
def raiz_quadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return 'Erro: Raiz quadrada de número negativo não é permitida.'

if __name__ == '__main__': 
    # Significa que o código só será executado se o arquivo for executado diretamente, e não quando for importado como um módulo.
    # Normalmente usado para testar funções ou variáveis definidas no arquivo.

    nome = 'Paulo'
    print(Senha == 1234)

    # Testando as funções
    print(saudações(nome))    
    print(soma(5, 3))
    print(subtração(10, 4))
    print(multiplicação(6, 7))
    print(divisão(20, 4))
    print(potência(2, 3))
    print(raiz_quadrada(16))