import Moeda

preço = float(input('Digite um preço: '))
print(f'A metade de {Moeda.moeda(preço)} é {Moeda.moeda(Moeda.metade(preço))}')
print(f'O dobro de {Moeda.moeda(preço)} é {Moeda.moeda(Moeda.dobro(preço))}')
print(f'Aumentando 10% temos {Moeda.moeda(Moeda.aumento(preço))}')