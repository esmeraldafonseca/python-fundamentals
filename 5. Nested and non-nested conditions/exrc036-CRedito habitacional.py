casa = float(input('Digite o valor da casa:'))
sal = float(input('Digite o seu salario actual:'))
anos = int(input('Digite em quantos anos queres pagar:'))
exss = sal * 0.30
prestação = casa / (anos*12)

if prestação > exss :
    print('A prestação mensal será de {}. O valor é superior a 30% do teu salario'.format(prestação))
    print('Credito não aprovado')

else :
    print('A prestação mensal será de {}.'.format(prestação))
    print('Credito aprovado')

