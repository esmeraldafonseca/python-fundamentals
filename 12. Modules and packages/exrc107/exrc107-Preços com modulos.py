import Moeda

preço = float(input('Digite um preço: '))
print(f'A metade de {preço:.2f} é {Moeda.metade(preço):.2f}')
print(f'O dobro de {preço:.2f} é {Moeda.dobro(preço):.2f}')
print(f'Aumentando 10% temos {Moeda.aumento(preço):.2f}')