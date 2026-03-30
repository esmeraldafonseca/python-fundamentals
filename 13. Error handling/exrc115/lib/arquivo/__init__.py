from exrc115.lib.interface import *

def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve algum ERRO com a criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(txt):
    try:
        a = open(txt, 'rt')

    except:
        print('ERRO com a leitura do arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for item in a:
            dado=item.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='DESCONHECIDO', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO com a gravação dos dados')
        else:
            print(f'O cadastro de {nome} foi feito com sucesso')
            a.close()


