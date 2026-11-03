from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('{:=^23}'.format('JOGO'))

print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada?'))

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')

print('=-' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jpgador jogou {}'.format(itens[jogador]))

if computador == 0 :
    if jogador == 0 :
        print('EMPATE')

    elif jogador == 1 :
        print('VENCESTE')

    elif jogador == 2 :
        print('PERDESTE')
    else:
        print('Opção invalida')

elif computador == 1 :
    if jogador == 0:
        print('PERDESTE')
    elif jogador == 1 :
        print('EMPATE')
    elif jogador == 2 :
        print('VENCESTE')
    else:
        print('Opção invalida')

elif computador == 2 :
    if jogador == 0:
        print('VENCESTE')
    elif jogador == 1 :
        print('PERDESTE')

    elif jogador == 2 :
        print('EMPATE')
    else:
        print('Opção invalida')



print('=-'*15)
