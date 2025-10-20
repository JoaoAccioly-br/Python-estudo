with open('Manipulação de Arquivos/CSV para Dicionário/desafio.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
chaves = lines[0].strip('\n').split(';')
dados = {}
for c in chaves:
    dados[c] = []
for l in lines[1:]:
    valores = l.strip('\n').split(';')
    for i in range(len(chaves)):
        dados[chaves[i]].append(valores[i])
print(dados['nome'])
print(dados['idade'])
print(dados['endereco'])