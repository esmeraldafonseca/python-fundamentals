print('=' * 30)
print('{:^25}'.format('Banco EF'))
print('=' * 30)

valor = int(input('Digite o valor que queres sacar: '))
notas50 = valor % 50

while True:
    if notas50 >=0:
        print(f'vais precisar {notas50 :.2f} de 50')

  """  if valor =0:
        break"""

