# Podemos usar listas para implementar pilhas (LIFO - Last In, First Out) e filas (FIFO - First In, First Out) em Python.
# A estrutura mais usada é os dicionários, que são implementados como tabelas hash.

# Pilha (LIFO)

stack = [] # Cria a Pilha
stack.append(10) # Empilha o valor 10
stack.pop() # Retira o valor do topo

# Fila (FIFO)

from collections import deque

queue = deque() # Cria uma Lista duplamente encadeada pois assim facilita a retirada no ínicio da fila
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft() # Retira o primeiro valor da
print(queue)

# Também temos três estruturas não abordadas nas variáveis compostas, que são:

# Os dicionários (Que tem implantado uma Hash Table)

hash_map = {} # Declaração de um dicionário ou pode ser {chave:valor, chave:valor}
hash_map['Paulo'] = 'Estudante' # Dicionário usa uma estrutura de (chave,valor) onde a chave é única e str ou int
print(hash_map['Paulo'])
hash_map['Paulo'] = 'Estágiario' # Caso coloque a chave que já existe, o valor é subscrito
print(hash_map['Paulo'])
hash_map['Julio'] = 'Motorista'
hash_map['Ailson'] = 'Analista de sistemas'
hash_map['Joao'] = 'Analista de estoque'
hash_map['Jose'] = 'Motoboy'
print(hash_map.keys()) # Retorna uma lista com as chaves
print(hash_map.values()) # Retorna uma lista com os valores
print(hash_map.items()) # Retorna uma lista de tuplas com (chave,valor)
print(hash_map)

# Ex:

Pessoas = ({'Nome':'Paulo', 'Idade':25, 'Profissão':'Estudante'},
           {'Nome':'Julio', 'Idade':30, 'Profissão':'Motorista'},
           {'Nome':'Ailson', 'Idade':28, 'Profissão':'Analista de sistemas'} )
Pessoas[0]['Nome'] = 'João'
print(Pessoas)

Joao = {'Nome':'Joao',
        'Idade':22,
        'Profissão':[
            {'Cargo':'Analista de estoque',
            'Empresa':'Magazine Luiza'},
            {'Cargo':'Estagiario',
            'Empresa':'Loja Americanas'},
            {'Cargo':'Auxiliar de estoque',
            'Empresa':'Carrefour'}]
        }
print(Joao['Profissão'][0]['Empresa'])
print(Joao)

# As Tuplas (Que são estruturas imutáveis)

Tuple = "joao" , "paulo" , "julio" # Declaração de Tuplas, mas pode ser por parenteses também
print(Tuple)
'''Tuple.apppend(10) # Erro pois não é possível alterar
Tuple.pop() # Mesmo erro'''
print(Tuple.count('joao'))

Tuple2 = ([10,20,30], [100,200,300]) # Pode existir tuplas de objetos mutáveis
Tuple2[0].append(40) # Pode realizar todos os métodos que uma lista pode receber
print(Tuple2)
'''Tuple2[0] = [0,1,2] # Erro pois não pode alterar Tupla'''



# Os Sets ou conjuntos: Tem como característica não permitir valores iguais

Sets = {1,2,3} # Declaração de um set
Sets2 = {2,3,4}
Sets.add(4)
print(Sets)
teste = Sets.union(Sets2)  # União de dois sets, não tem valores repetidos
print(f'Essa é o novo set {teste}')
Sets.difference(Sets2) # Set tem métodos de conjuntos matemáticos como igual, diferente e etc
Sets.intersection(Sets2)
# Essas são as principais estruturas de dados básicas em Python.


