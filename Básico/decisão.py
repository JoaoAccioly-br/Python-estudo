# Estruturas de decisão (If, Else, Elif, Match)

# If - Serve para decisões mais simples, é executado quando a condição é atendida. Ex: se o valor for maior q 6 ele passa de ano

nota = int(input('Insira um valor de 1 a 10: '))

if nota % 2 == 0:
    print('O número é par!')

# Else - Serve para decisões compostas, é executada quando o if não é atendido. Ex: Valor é par ou ímpar

nota = int(input('Insira um valor de 1 a 10: '))

if nota % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')

# Elif - Serve para ter Ifs aninhados. Ex: se for maior é x, se for menor é y, mas se for igual é z

nota = int(input('Insira um valor de 1 a 10: '))

if nota >= 6:
    print('Passou de semestre!')
elif nota <= 5 and nota > 0:
    print('Não passou de semestre!')
elif nota == 0:
    print('Zerou o semestre')

# Match - Funciona da mesma forma que um elif, mas mais organizado e com restrições

opcao = input('Escolha uma opção (1 = 10 / 2 = 20 / 3 = 30): ')

match opcao:
    case 1:
        print('O valor escolhido foi 10!')
    case 2: 
        print('O valor escolhido foi 20!')
    case 3: 
        print('O valor escolhido foi 30')
    case _:
        print('A opção escolhida não existe!')


