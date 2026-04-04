import datetime
ano = int(input('Digite o seu ano de nascimento:'))
genero = str(input('Digite M para masculino e F para feminino:')) .strip() .upper()
data = datetime.date.today().year
idade = data - ano

if genero == 'F' :
    print('Mulheres nã precisam se alistar')

elif idade == 18:
    print('Tens que se alistar IMEDIATAMENTE')

elif idade < 18 :
    print('ainda falta para alistar')
    saldo = 18 - idade
    print('faltam {} anos para t alistares'.format(saldo))
    hj = data + saldo
    print('no ano de {}'.format(hj))

else:
    print('Ja devias ter t alistado, mais velho burro...')
    saldo = idade - 18
    print('devias ter t alistado a {} anos'.format(saldo))
    hj = data - saldo
    print('no ano de {}'.format(hj))

