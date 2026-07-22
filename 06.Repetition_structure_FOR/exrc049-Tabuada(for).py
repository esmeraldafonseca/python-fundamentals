n1 = int(input('Digite um número para ver a sua tabuada:'))

print('{:=^36}'.format('Tabuada'))
for n in range(0, 13):
    print('{:2} X {} = {:2}'.format(n, n1, n*n1))


