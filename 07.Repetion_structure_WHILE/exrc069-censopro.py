
print('=' * 20)
print('Cadastro')
print('=' * 20)

sexo = ' '
escolha = 'S'
age = 0
maior =  menos = men = 0

while True :

    age = int(input('Idade: '))
    if age >= 18 :
        maior += 1

    sexo = str(input('Sexo[M/F]:')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]:')).strip().upper()[0]
    if sexo == 'M':
        men += 1
    if age < 20 and sexo == 'F':
        menos += 1

    escolha = str(input('Quer continuar?[S/N]')) .strip() .upper()
    print('*' * 30)

    if escolha != 'S' :
        break


print(f'''Cadastramos {maior} pessoas maiores de de idade
{men} Homens 
{menos} mulheres menores de 20 anos
''')
print('fim')