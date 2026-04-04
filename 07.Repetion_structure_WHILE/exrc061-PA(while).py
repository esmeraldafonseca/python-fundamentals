n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão:'))
n10 = 1


while n10 <= 10 :
    n1 += r
    print('{}, ' .format(n1), end='')
    n10 += 1


print('FIM')

