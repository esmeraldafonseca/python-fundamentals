def verificação(nomes = "<<Desconhecido>>", gol =0):
    """
    Verificaçaõ do desempenho dos jogadores no campeonato
    :param nome:(OPCIONAL) nome do jogados
    :param gol: (OPCIONAL) quantos gols ele fez
    :return: Os dados estilizados do jogador
    """
    return f'O Jogador {nomes} fez {gol}'


#programa principal
nome = str(input("Nome do Jogador: "))
gols = str(input("Numero de gols:  "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols=0

if nome.strip() =='':
    print(verificação(gol=gols))
else:
    print(verificação(nome, gols))

