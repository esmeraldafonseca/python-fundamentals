from random import randint

n = s = c = 0
titulo = 'Par ou impar'
rand = randint(1, 9)
print('=' *30)
print(f'{titulo:^27}')
print('=' *30)


while True :
    escolha = str(input('PAR ou IMPAR:')).strip() .upper()
    n = int(input('Digite o número:'))
    if escolha == 'IMPAR':
        if (n + rand) % 2 != 0:
            print(f'''GANHASTE
            Eu escolhi {rand} e tu {n} ''')
        elif (n + rand) % 2 != 0:
            print(f'''PERDESTE
            Eu escolhi {rand} e tu {n} ''')
            break

   ''' elif escolha == 'PAR':
        if (n + rand) % 2 == 0 :
            print(f'''GANHASTE
            Eu escolhi {rand} e tu {n} ''')
        elif (n + rand) % 2 == 0 :
            print(f'''PERDESTE
            Eu escolhi {rand} e tu {n} ''')
            break

print('FIM')
'''


