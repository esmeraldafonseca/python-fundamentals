def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31m ERRO. Por favor digite um numero inteiro valido!\033[m')
        except(KeyboardInterrupt):
            print('ERRO. Campo vazio!')
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for itens in lista:
        print(f'{c} - {itens}')
        c += 1
    print(linha())
    opç = leiaInt('A sua opção é: ')
    return opç