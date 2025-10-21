import requests
import json

api = 'https://viacep.com.br/ws/{cep}/json/'
dados = []
ceps = []

def ler_ceps():
    for _ in range(3):
        teste = input('Digite o cep desejado: ')
        ceps.append(teste)

ler_ceps()

for i in range(len(ceps)):
    resposta = requests.get(api.format(cep=ceps[i]))
    if resposta.status_code == 200:
        dados.append(resposta.json())
    elif resposta.status_code >= 400:
        print(f'Erro ao consultar o cep {ceps[i]}: {resposta.status_code}')
print(dados)

with open('Testes api\ceps\ceps.json', 'w', encoding='utf-8') as open_archive:
    json.dump(dados,open_archive,ensure_ascii=False, indent=4)
    
with open('Testes api\ceps\ceps.json', 'r', encoding='utf-8') as read_archive:
    conteudo = json.load(read_archive)
    for i in range(len(conteudo)):
        print(conteudo[i]['logradouro'])