def votação(ano):
    """
       Função que verifica se o usuario tem voto obrigatorio,
       opcional ou ate mesmo não vota
       :param ano: ano de nascimento
       :return: um valor liteal mostrando se pode ou n votar
       """
    from datetime import datetime
    anos = datetime.now().year - ano
    if anos < 18:
        return f'Com {anos}: NÃO VOTA'
    elif anos >= 18 and anos < 60:
        return f'Com {anos}: VOTA OBRIGATORIA'
    elif anos >= 65:
      return f'Com {anos}: VOTO OPCIONAL'


#Programa principal
ano = int(input("Ano de nascimento: "))
print(votação(ano))
