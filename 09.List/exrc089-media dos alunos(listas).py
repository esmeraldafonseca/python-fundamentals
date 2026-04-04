dados= []
resposta = "S"
parar = 999


while resposta == "S":
    nome= str(input("Nome: "))
    notas0=float(input("Nota 1:"))
    nota1=float(input("Nota 2:"))
    media = (notas0 + nota1)/2
    dados.append([nome, [notas0, nota1], media])
    resposta = str(input("Quer continuar? [S/N]")).upper()

print("-=" * 30)


print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print("-"*30)

for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print("-"*30)

while True:
    parar = int(input("Mostrar nota de qual aluno?Digite 999 para sair:"))
    if parar == 999:
        break
    if parar <= len(dados) - 1:
        print(f'Notas de {dados[parar][0]} são {dados[parar][1]}')
        print()
