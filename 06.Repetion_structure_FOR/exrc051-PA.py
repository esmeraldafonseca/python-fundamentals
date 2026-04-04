print('='*30)
print('{: ^10}'.format('PROGRESSAO ARITMETRICA'))
print('='*30)

n1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão'))
decimo = n1 + (10 - 1) * r
for n in range(n1, decimo + r, r):
    print(n, end=' ')

