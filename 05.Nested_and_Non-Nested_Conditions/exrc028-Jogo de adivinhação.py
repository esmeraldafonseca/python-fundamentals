from random import randint
from time import sleep
print('-==' *23)
print('Eu vou pensar em um número entre o e 5, tenta adivinhar qual foi')
print('-==' *23)

n = randint(1, 5)
n1 = int(input('Digite o seu número: '))
print('PROCESSANDO...')
sleep(2)

if n1 == n :
    print('Acertaste, PARABENS!')
else:
    print('Erraste, eu pensei no número: {} e não no: {}'.format(n, n1))

print('-==' *23)
