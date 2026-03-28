def metade(n=0, moed=False):
    res= n/2
    if moed:
        return moeda(res)
    return res


def dobro(n=0, moed=False):
    res = n * 2
    return res if moed is False else moeda(res)


def aumento (n=0, taxa = 0, moed =False):
    res = n + (n * taxa/100)
    return res if moed == False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{n:.2f} {moeda}'.replace('.',',')


def dimunuir (n=0, taxa =10, moed=False):
   res = n - (n * taxa/100)
   return res if not moed else moeda(res)


def resumo(n=0, aum=20, dimi=5):
    print("-"*30)
    print('RESUMO DO VALOR'.center(30))
    print("-"*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{aum}% de aumento: \t{moeda(aumento(n, aum))}')
    print(f'{dimi}% de diminuição: \t{moeda(dimunuir(n, dimi))}')
