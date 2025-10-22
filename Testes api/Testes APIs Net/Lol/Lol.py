import requests
import json

champion = input('Insert a character name:').capitalize()
url = 'https://ddragon.leagueoflegends.com/cdn/15.20.1/data/pt_BR/champion/{champion}.json'

response = requests.get(url.format(champion=champion))
if response.status_code == 200:
    data = response.json()
elif response.status_code >= 400:
    print('Character not found')

with open(f'Testes api/Testes APIs Net/Lol/{champion}.json', 'w', encoding='utf-8') as create_file:
    json.dump(data,create_file, ensure_ascii='utc-8', indent=4)

with open(f'Testes api/Testes APIs Net/Lol/{champion}.json', 'r', encoding='utf-8') as open_file:
    content = json.load(open_file)
    print(content['data'][champion].keys())