n = int(input('Digite o [999] para parar: '))
contador = 0

while n != 999 :
    contador += n
    n = int(input('Digite o [999] para parar: '))



print('A soma de todos os numeros digitados é: {}'.format(contador))
