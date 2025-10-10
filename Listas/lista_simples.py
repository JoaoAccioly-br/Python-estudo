agenda = []

def inserir_lista():
    nome = input("Insira o nome que deseja colocar na agenda: ")
    if nome in agenda:
        print('Erro: o nome já existe na lista.')
        print(f'A lista continua {agenda}')
        return
    else:
        agenda.append(nome)
    print(agenda)

for i in range(3):
    inserir_lista()