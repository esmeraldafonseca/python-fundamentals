from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('{:=^23}'.format('JOGO'))

print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
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

if computador == 1 :
    if jogador == 1 :
        print('EMPATE')

    elif jogador == 1 :
        print('VENCESTE')

    elif jogador == 2 :
        print('PERDESTE')
    else:
        print('Opção invalida')

elif computador == 1 :
    if jogador == 0:
        print('VENCESTE')
    elif jogador == 1 :
        print('EMPATE')
    elif jogador == 2 :
        print('PERDESTE')
    else:
        print('Opção invalida')

elif computador == 2 :
    if jogador == 0:
        print('PERDESTE')
    elif jogador == 1 :
        print('VENCESTE')

    elif jogador == 2 :
        print('EMPATE')
    else:
        print('Opção invalida')



print('=-'*15)
