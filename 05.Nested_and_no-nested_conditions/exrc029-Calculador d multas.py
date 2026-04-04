v = float(input('digite a velocidade do carro'))

if v > 80:
    print('Vais ver multado cabrão')
    multa = v - 80
    print('e a multa será de {:.2f}' .format(multa * 7))

print('FIIIM')