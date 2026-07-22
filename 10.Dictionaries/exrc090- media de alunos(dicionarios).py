
dados = dict()

dados['Nome'] = str (input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}:'))


print("-="*30)

if dados['Media'] <= 4:
    dados['Situação'] = 'Reprovado/a'

else:
    dados['Situação'] = 'Aprovado/a'

for k, v in dados.items():
    print(f'    -{k} é igual a {v}')

print("-="*30)
