import Moeda

preço = float(input('Digite um preço: '))
print(f'A metade de {Moeda.moeda(preço)} é {Moeda.metade(preço, True)}')
print(f'O dobro de {Moeda.moeda(preço)} é {Moeda.dobro(preço, True)}')
print(f'Aumentando 10% temos {Moeda.aumento(preço, 10, True)}')