km = float(input('Digite a quantidade de km percorrida'))
dias = float(input('Digite os dias usados'))
kmv = float(km * 0.15)
diasv = float( dias * 60)
valor = float(kmv + diasv)

print('o valor a pagar é {:.2f}' .format(valor))
