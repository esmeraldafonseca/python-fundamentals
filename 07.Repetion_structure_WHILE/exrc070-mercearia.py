print('='*20)
print('Cantina')
print('='*20)
maior = cont = total = menor = 0
barato  = ' '

while True:

    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço do produto: '))
    total += preço
    cont += 1

    if cont == 1:
        menor = preço
        barato = nome
    elif menor > preço:
        menor = preço
        barato = nome


    if preço > 1000:
        maior += 1

    escolhas = ' '
    while escolhas not in 'SN':
        escolhas = str(input('Quer continuar?[S/N]')).strip() .upper()
    if escolhas != 'S':
        break

print('{:-^40}'.format('fim'))
print(f'''O total das compras foi de {total:.2f} KZ
e teve {maior} produtos q custavam mais que 1000
o produto mair barato foi {barato}
''')


