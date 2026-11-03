print('=' * 30)
print('{:^25}'.format('Banco EF'))
print('=' * 30)

valor = int(input('Digite o valor que queres sacar: '))
total = valor
nota = 50
qtd = 0

while True:
    if total >= nota:
        total -= nota
        qtd += 1
    else:
        if qtd > 0:
            print(f'vais precisar {qtd} nota(s) de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        qtd = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao Banco EF!')
