def factorial(numero, show='False'):
    """
    Um programa que mostra o factorial de um numero
    :param numero:O numero para calcular o factorial
    :param show:True caso queria ver o calculo e False senão(opcional)
    :return: o valor do factorial do numero
    """
    c=1
    for i in range(1, numero + 1):
        c *=i
        if show:
            print(f'{i}', end='')
            if i < numero:
                print(f' x ', end='')
            else:
                print(f' = ', end='')

    return c


#Programa principal
print(factorial(5, True))