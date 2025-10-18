import funções

print(funções.nome) # A váriavel 'nome' está definida no if __name__ == '__main__' do arquivo funções.py, por isso não pode ser acessada aqui.

print(funções.Senha) # A váriavel 'Senha' está definida no arquivo funções.py, por isso pode ser acessada aqui.
print(funções.Email)

print(funções.saudações('Fernando')) # A função 'saudações' está definida no arquivo funções.py, por isso pode ser acessada aqui.
print(funções.potência(2, 3))
print(int(funções.raiz_quadrada(16)))

