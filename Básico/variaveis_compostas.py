# As variáveis também podem ser compostas, ou seja, ter mais de 1 valor
# Para isso, utilizamos listas

idades = [12,17,25,14,87]
nomes = ['joao','pedro','julio','luiz']
usuario = ['joao',25,'solteiro',True]
comidas = [] # Uma lista vazia

# Listas podem ter valores de diversos tipos dentro, mas sempre será do tipo lista

type(idades)
type(usuario)

# Para buscar um valor em uma lista, se é utilizado o índice

print(idades[3]) # 14
print(nomes[0]) # joao

# Também é possível pesquisar por fatiamento (Uma porção da lista)

print(idades[0:2]) # [12 , 17] não se é pegado o valor do índice 2 (Continha básica: 2 - 0 = 2 valores)
print(idades[:2) # mesmo retorno
print(idades[2:]) # vai do indice 2 até o final

# Caso seja números, é possível realizar operações dentro

print(sum(idades)) # Soma deles
print(min(idades)) # Menor idade
print(max(idades)) # Maior idade

# Também é possível tirar o tamanho das listas

print(len(idades))
print(len(nomes))
print(len(usuario))

# Uma lista pode ter uma lista dentro ela

nomes2 = [['paulo','fabio','claudio'],['maria','ana','joana']]
print(len(nomes2)) # 2
print(nomes2[0][2]) # fabio

# Para colocar e retirar de forma dinâmica, podemos usar os métodos append e pop

comidas.append('batata')
comidas.append('macarrão')
comidas.append('alface')

print(comidas) 

comidas.pop() # Retira o alface, pois pop retira o último valor
comidas.remove('batata') # Retira batata

# Também é possível inserir por index

idades.insert(2,5) # Insere na posição 2 o valor 5

# Também é possível organizar e inverter uma lista

nomes.sort() # Coloca em ordem alfabética
nomes.reverse() # Inverte a ordem da lista ou nomes[::-1]

# Exemplo

def media_notas():
  notas = []
  
  for x in range(4):
    n = input(f"insira a sua nota do bimestre {i+1}")
    notas.append(n)
  return sum(notas) / len(notas)

def quantos_produtos():
  total = 0
  lista = [1,2,6,7,8,5,4,3,5,1,5,6,2,5,4,6,2,1,2,3,0,6,7,0]
  num = int(input('insira o número que deseja saber'))
  for n in lista:
    if n == num:
      total += 1
  print(total)
quantos_produtos()
 # OU

lista = [1,2,6,7,8,5,4,3,5,1,5,6,2,5,4,6,2,1,2,3,0,6,7,0]
num = int(input('insira o número que deseja saber'))
lista.count(num)



