

cont = soma = m = n = mr = mnr = 0
r = 's'

while r in 'Ss' :
    n = int(input('digite um numero:'))
    r = str(input('quer continuar? [S/N]:'))
    soma += n
    cont += 1
    if cont == 1:
        mr = mnr = n
    else:
        if n > mr :
            mr = n
        elif n < mnr :
            mnr = n



m = soma / cont
print('A soma dos numeros digitados é {} e a media é {}'.format(soma, m))
print('O maior é {} e o menor é {}'.format(mr, mnr))
