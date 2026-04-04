from math import factorial

n1 = int(input('Digite um número para saber o seu Fatorial: '))
contador = n1
f = factorial(n1)

while contador > 0:
    print('{}'.format(contador), end='')
    if contador > 1:
        print(' X', end=' ')
    else:
        print(' = {}'.format(f))
    contador -= 1

print('fim')