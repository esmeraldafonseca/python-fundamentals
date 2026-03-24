n = 0

while True :
    n =int(input('Digite um valor positivo para ver a sua tabuado:'))
    if n < 0 :
        break

    print('*' * 20)
    for a in range (1, 11):

        print(f'''{n} X {a} = {n*a} ''')
    print('*' * 20)


print('Comando invalido')