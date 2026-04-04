maior = 0
menor = 0
for n in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(n)))
    if n == 1 :
       menor = peso
       maior = peso
    else:
        if peso < menor :
            menor = peso

        if peso > maior :
            maior = peso

print('O maior peso digitado foi {:.1f} e o menor foi {:.1f}'.format(maior, menor))

