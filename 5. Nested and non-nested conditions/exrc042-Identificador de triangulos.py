r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceira segmento: '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2 :
    print('É possivel formar um triangulo.')
    if r1 == r2 == r3:
        print('É um triangulo equilatero')

    elif r1 != r2 != r3 != r1:
        print('É um triangulo isoceles')

    else:
        print('Escaleno')

else:
    print('Não pode formar um triangulo')


'''
elif r1 == r2 or r1 == r3 or r2 == r3 :
    print('É um triangulo isosceles')

else:
    print('É um triangulo escaleno')
'''