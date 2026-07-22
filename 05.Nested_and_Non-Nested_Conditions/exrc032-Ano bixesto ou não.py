from datetime import date

ano = int(input('digite o ano. coloque 0 para analisar o ano actual:'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 400 == 0 or ano % 100 !=0 :
    print('o ano {} é bixesto'.format(ano))
else:
    print('o ano não é bixesto')