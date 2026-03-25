Itens = ("Lapis", 1.50,
         "Borracha", 2,
         "Caderno", 5,
         "Estogio", 7.50)

print("-"*40)
print(f'{"Papelaria":^40}')
print("-"*40)

for pos in range(0, len(Itens)):
    if pos % 2 == 0:
        print(f'{Itens[pos]:.<30}', end='')
    else:
        print(f'{Itens[pos]:>7.2f}')
print("-"*40)