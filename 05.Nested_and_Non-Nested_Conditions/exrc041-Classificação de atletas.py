from  datetime import date

ano = int(input('Digite o seu ano de nascimento: '))
data = date.today().year
idade =  data - ano

print('Nasceste no ano de {} e tens {}'.format(ano, idade))

if idade <= 9 :
    print('Pertences a categoria: MIRIM')

elif idade >= 14 and idade > 9 :
    print('Pertences a categoria: INFANTIL')

elif idade >= 19 and idade > 14 :
    print('Pertences a categoria: JUNIOR')

elif idade >= 20 and idade > 19 :
    print('Pertences a categoria: SENIOR')


