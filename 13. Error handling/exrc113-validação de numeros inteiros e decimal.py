def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31m ERRO. Por favor digite um numero inteiro valido!\033[m')
        except(KeyboardInterrupt):
            print('ERRO. Campo vazio!')
        else:
            return f'O numero intero digitado foi {n}'


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO. Por favor digite um numero inteiro valido!\033[m')
        except(KeyboardInterrupt):
            print('\033[31m ERRO. Campo vazio!\033[m')
        else:
            return f'O numero decimal digitado foi {n}'


#programa principal
n = leiaInt("Digite um numero interio: ")
n1 = leiaFloat("Digite um numero decimal: ")