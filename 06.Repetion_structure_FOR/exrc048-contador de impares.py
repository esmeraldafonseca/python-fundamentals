soma = 0
cont = 0

for n in range(1, 501, 2):
    if n % 3 == 0:

        soma += n
        cont += 1

print('Entre 1 e 500 temos {} impares diviseis por 3 e a soma deles é: {}'.format(cont, soma))


