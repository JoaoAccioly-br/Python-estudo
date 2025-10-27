import requests
import json

character = "albedo".capitalize()

url = "https://genshin.jmp.blue/characters/{character}?lang=pt"
pedido = requests.get(url.format(character=character))
print(pedido.json().keys())

