
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezasseis')


while True:  # loop principal
    while True:
        escolha = int(input('Digite um número entre 0 e 16: '))
        if escolha >= 0 and escolha <= 16:
            break
        else:
            print('Número inválido. Tente novamente.')

    print(f'Você digitou o número {numeros[escolha]}')

    continuar = input('Queres continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('Programa terminado.')