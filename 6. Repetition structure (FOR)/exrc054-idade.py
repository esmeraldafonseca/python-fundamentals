from datetime import date
menor = 0
maior = 0
data = date.today().year

for n in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(n)))
    idade = data - ano

    if idade >= 21 :
        maior += 1
    else:
        menor += 1

print('{} pessoas ja atigiram a maior idade e {} ainda não'.format(maior, menor))
