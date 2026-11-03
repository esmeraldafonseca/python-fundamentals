n1 = int(input('Digite um número para ver a sua tabuada:'))

print('{:=^36}'.format('Tabuada'))
for n in range(1, 11):
    print('{} X {:2} = {}'.format(n1, n, n*n1))


