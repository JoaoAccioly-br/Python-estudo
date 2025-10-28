import requests
import json

url = "https://genshin.jmp.blue/characters/{character}?lang=en"
characters = []
data = []

def Get_Names():
    num = int(input("How many characters u wanna search? "))
    for i in range(num):
        name = input("Insert the name of character you want: ").lower()
        characters.append(name)

def Search_Characters():
    for i in range(len(characters)):
        pedido = requests.get(url.format(character=characters[i]))
        if pedido.status_code == 200:
            data.append(pedido.json())
        elif pedido.status_code >= 400:
            print(f"Não foi possível ver o personagem {characters[i]}: {pedido.status_code}")

def Create_Files():
    for i in range(len(characters)):
        with open(f"Testes api/Testes APIs Net/Genshin/{characters[i]}.json","w",encoding="utf-8") as new_file:
            json.dump(data[i],new_file,ensure_ascii=False,indent=4)
            
def Read_Files():
    print(f"Characters data: {characters}")
    name = input("Insert the name of character u wanna read: ").lower()
    with open(f"Testes api/Testes APIs Net/Genshin/{name}.json","r",encoding="utf-8") as open_file:
        content = json.load(open_file)
        print(content.keys())

def Delete_Files():
    import os

    print(f"Characters searched: {characters}")

    teste = input("U wanna delete a single file or all files? (s/a) ").lower()
    if teste == "s":
        name = input("Insert the name of character u wanna delete: ").lower()
        os.remove(f"Testes api/Testes APIs Net/Genshin/{name}.json")
    elif teste == "a":
        for i in range(len(characters)):
            os.remove(f"Testes api/Testes APIs Net/Genshin/{characters[i]}.json")
    



