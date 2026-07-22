d = float(input('Digite a distancia em km'))

if d <= 200:
    preço = d * 0.50
    print('o preço da passagem é {}' .format(preço))
else:
    preço = d* 0.45
    print('o preço da passagem é {}'.format(preço))
