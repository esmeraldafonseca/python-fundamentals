print('{:=^39}'.format('loja'))
preço = float(input('Digite o valor do produto: '))

print('''Formas de pagamento
[1]- A vista com dinheiro
[2]- a vista no cartão
[3]- Até 2X no cartão
[4]- 3X ou mais no cartão

''')
opção = int(input('Digite a forma de pagamento: '))

if opção == 1 :
    desc = preço*0.10
    print('recebeste um desconto de 10% e so pagarás {}'.format(preço - desc))

elif opção == 2 :
    desc = preço * 0.05
    print('recebeste um desconto de 5% e so pagarás {}'.format(preço - desc))

elif opção == 3 :
    print('não tens desconto nenhum')

elif opção == 4 :
    aum = preço * 0.20
    print('pagarás um valor total de {}'.format(aum + preço))

else:
    print('opcao invalida'
          '')