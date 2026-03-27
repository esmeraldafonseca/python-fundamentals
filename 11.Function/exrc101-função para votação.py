def votação(ano=0):
    """
    Função que verifica se o usuario tem voto obrigatorio,
    opcional ou ate mesmo não vota
    :param ano: ano de nascimento
    :return: sem retorno
    """

    from datetime import datetime
    
    anos = datetime.now().year - ano
    if anos < 18:
        print(f'Com {anos}: NÃO VOTA')
    elif anos >= 18 and anos < 60:
        print(f'Com {anos}: VOTA OBRIGATORIA')
    elif anos >= 65:
        print(f'Com {anos}: VOTO OPCIONAL')


#programa principal
print("-"*30)
ano = int(input('Ano de nascimento: '))
votação(ano)
