n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão:'))
n10 = 1
nt = 10
mais = 10
while mais !=0:

    while n10 <= nt :
        print('{}, ' .format(n1), end='')
        n1 += r
        n10 += 1
    mais = int(input('Quantos termos tu queres ver mais:'))
    nt += mais

print('FIM')
