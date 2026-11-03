from random import randint

v = 0
titulo = 'Par ou impar'
print('=' *30)
print(f'{titulo:^27}')
print('=' *30)


while True :
    escolha = ' '
    while escolha not in ('PAR', 'IMPAR'):
        escolha = str(input('PAR ou IMPAR:')).strip() .upper()
    n = int(input('Digite o número:'))
    rand = randint(0, 10)
    total = n + rand
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    print(f'Eu escolhi {rand} e tu {n}. Total {total} deu {resultado}')
    if escolha == resultado:
        print('GANHASTE')
        v += 1
    else:
        print('PERDESTE')
        break

print(f'FIM. Ganhaste {v} vez(es) seguidas')
