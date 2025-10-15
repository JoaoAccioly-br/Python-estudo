# Funções de repetição (For / While)

# For - Realiza uma repetição de acordo com um número de vezes definido
# Existe 2 tipos básicos, usando range e usando uma lista
'''
Usando range

for i in range(5): # Cria uma variável de controle e anda 5 vezes (de 0 a 4)
    print(i)
'''
# A função range pega um número e cria um objeto iniciando a 0 até o número indicado - 1
# o "in" significa que ele vai andar em cada um dos itens em uma iterável (nesse caso o range)

'''
Usando uma lista

lista = ['batata','maça','uva','pera','abacate']

for i in lista:
    print(i)
'''

# While - Realiza uma repetição enquanto uma condição for atendida
'''
num = 10

while num > 6:
    num = int(input('Insira um número de 1 a 10: '))

'''

# Loop infinito, só para quando o break for acionado
'''
while True: 
    num = int(input('Insira um número de 1 a 10: '))
    if num < 1 or num > 10:
        print('Número inválido, tente novamente!')
    else:
        print('Número válido!')
        break
'''
