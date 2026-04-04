print('=' *30)
print('Sequensecia de Fibonate')
print('=' * 30)

n = int(input('Digite quantos termos queres ver:'))
contador = 0
t1 = 0
t2 = 1

print('~' * 30)

print('{} » {}'.format(t1, t2), end='')
while contador < n :

    t3 = t1 + t2
    print(' » {} '.format(t3), end='')
    contador +=1
    t1 = t2
    t2 = t3

print('» FIM.')