# Declaração de variáveis
# nome = valor
'''
nome = 'paulo' #String
numero = 123456789 #Int
existe = True #Bool
altura = 1.75 #Float
'''
# Váriaveis locais e globais

'''Media = 0 #Variável global
total = 0 #Variável global

def media_nota():
    global Media, total #Para acessar uma variável global é só colocar (global variável)
    for i in range(4):
        nota = int(input('Insira a nota nos 4 bimestres: ')) #Variável local
        total += nota # Para realizar essa soma por meio de somente variáveis, precisa ser declarado antes
        Media = total / 4
    print(Media) # Retorna str

media_nota()
'''

'''
num = int(input('Insira um número')) # Transforma o input string em int
num2 = float(input('Insira um número com vírgula')) # Transforma o input string em float    
'''

'''
num = 10
num2 = 3

print(num // num2) # Retorna somente o valor inteiro da divisão!
'''