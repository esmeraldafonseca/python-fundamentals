from exrc115.lib.interface import *
from exrc115.lib.arquivo import *
from time import sleep

arq = 'Python'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Mostrar pessoas', 'Cadastrar novas pessoas', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        cabeçalho('ERRO! Digite uma opção valida')
    sleep(2)