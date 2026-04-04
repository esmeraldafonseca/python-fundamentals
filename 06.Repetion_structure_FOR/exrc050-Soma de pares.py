cont = 0
soma = 0
for n in range(1, 7):
    n1 = int(input('Digite o {}º numero:'.format(n)))
    if n1 % 2 == 0 :
        soma += n1
        cont += 1

print('Tu digitaste {} pares, e a soma deles foi {}'.format(cont, soma))

