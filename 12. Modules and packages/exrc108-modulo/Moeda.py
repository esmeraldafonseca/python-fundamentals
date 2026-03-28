def metade(n=0, moeda=False):
    res= n/2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumento (n=0, taxa = 0):
    res = n + (n * taxa/100)
    return res


def moeda(n=0, moeda='R$'):
    return f'{n:.2f} {moeda}'.replace('.',',')


def dimunuir (n=0, taxa =10):
   res = n - (n * taxa/100)
   return res
