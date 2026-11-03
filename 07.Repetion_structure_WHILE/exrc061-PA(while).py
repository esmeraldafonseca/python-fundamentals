n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão:'))
n10 = 1


while n10 <= 10 :
    print('{}, ' .format(n1), end='')
    n1 += r
    n10 += 1


print('FIM')

