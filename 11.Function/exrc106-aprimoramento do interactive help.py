from time import sleep

#Variavel global que vai receber todas as cores que vou usar
c= ('\033[m' ,         # 0 - Sem cor
    '\033[0;30;41m',   # 1 - Vermelho
    '\033[0;30;42m',   # 2 - Verde
    '\033[0;30;43m',   # 3 - Amarelo
    '\033[0;30;44m',   # 4 - Azul
    '\033[0;30;45m',   # 5 - Roxo
    '\033[7;30m'       # 6 - Branco
    )

def titulo(text, cor=0):
    print(c[cor], end='')
    print('~'* (len(text)+6))
    print(f'   {text}')
    print('~' * (len(text)+ 6))
    print(c[0], end='')
    sleep(1)


def ajuda(comando):
    titulo(f'A acessar o manuel de comandos...')
    sleep(1.5)
    print(c[6])
    help(comando)
    print(c[0])
    sleep(2)


#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca(FIM = sair): '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)


titulo('ATÉ BREVE', cor=1)


