
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))

print('Digite um dos numeros abaixo para realizar uma das ações marcadas')
k = 0

while k != 5 :
    k = int(input('''
           [1] SOMAR
           [2] MULTIPLICAR
           [3] MAIOR
           [4] NOVOS NUMEROS
           [5] SAIR DO PROGRAMA
           '''))
    if k == 1 :
        print('=' *20)
        print('SOMA')
        print('=' *20)
        print('{} + {} = {}'.format(n1, n2, n1+n2))

    elif k == 2:
        print('=' * 20)
        print('MULTIPLICAÇÃO')
        print('=' * 20)
        print('{} X {} = {}'.format(n1, n2, n1 * n2))

    elif k == 3 :
        print('=' * 20)
        print('MAIOR')
        print('=' * 20)
        if  n1 > n2 :
            print('{} > {}'.format(n1, n2))
        elif n2 > n1:
            print('{} > {}'.format(n2, n1))
        else:
            print('{} = {}'.format(n1, n2))

    elif k == 4 :
        print('=' * 20)
        print('INSIRA NUMEROS NOVOS')
        print('=' * 20)
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))

    elif k == 5:
        print('A sair do programa...')

    else:
        print('Opção invalida, digite novamente')


print('FIM')



