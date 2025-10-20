import json


with open('Manipulação de Arquivos/Lidando com json/exemplo.txt', 'r', encoding='utf-8') as a:
    conteudo=json.load(a)
    print(conteudo)
    print(conteudo['email'])

    
