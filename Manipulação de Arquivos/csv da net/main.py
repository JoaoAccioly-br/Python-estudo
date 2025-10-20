import pandas as pd

with open('Manipulação de Arquivos/csv da net/revised.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
chaves = lines[0].strip('\n').split(',')
print(chaves)
data = {}
for c in chaves:
    data[c] = []
for l in lines[1:]:
    valores = l.strip('\n').split(',')
    for i in range(len(chaves)):
        data[chaves[i]].append(valores[i])
tabela = pd.DataFrame(data)
tabela.to_csv('teste.csv')

