dados = {}
pessoas = []

media =0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo[F/M]: ')) .upper()[0] .strip()
    while sexo not in 'MF':
        print('Valor invalido! M Or F')
        sexo = str(input('Sexo[F/M]: ')).upper() .strip()
    else:
        dados['Sexo'] = sexo
    dados['Idade'] = int(input('Idade: '))
    media += dados['Idade']
    pessoas.append(dados.copy())

    resposta = str(input('Quer continuar? [S/N]: ')).upper() .strip()

    while resposta not in 'NS':
            print('Resposta invalida. Tente S or N')
            resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resposta == 'N':
            break

print('-='*30)
mediafinal = media/len(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A media de idades das pessoas cadastradas é {mediafinal:.2f}')
print(f'C) As mulheres cadastradas foram:', end='')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f"{p['Nome']}")
print(f'D) As pessoas que estão acima da media são:', end='')
for p in pessoas:
    if p['Idade'] > mediafinal:
        print(f"{p['Nome']} com {p['Idade']} anos")
print("        <<ENCERRADO>>")



