from os.path import split

n = int((input('Digite um nume de 0 a 9999:')))


u = n // 1 % 10
d = n //10 %10
c = n // 100 % 10
m = n // 1000 % 10



print('Unidades: {}' .format(u))
print('Dezenas: {}' .format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}' .format(m))