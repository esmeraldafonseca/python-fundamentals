n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))

if n1 > n2 :
    print('{} é maior'.format(n1))
elif n2 > n1 :
    print('{} é o maior'.format(n2))
else :
    print('Eles são iguais')
