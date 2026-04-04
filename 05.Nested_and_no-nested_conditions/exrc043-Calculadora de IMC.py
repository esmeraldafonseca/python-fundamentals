peso = float(input('Digite o seu peso (Kg):'))
altura = float(input('Digite a sua altura(m):'))

imc =  peso / (altura**2)

print('O teu IMC é de: {:.2f}'.format(imc))

if imc < 18.5 :
    print('Estás abaixo do peso.')

elif imc >= 18 and imc <= 25:
    print('Estás no peso ideal')

elif imc > 25 and imc >= 30:
    print('Está com sobrepeso')

elif imc > 30 and imc >= 40 :
    print('Estás com obesidade')

else:
    print('Estás com obesidade morbida')

