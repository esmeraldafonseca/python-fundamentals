pessoas = []
dados = []
resposta = "S"

pesado = 0
leve = 0

while True:

    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))

    # Primeira pessoa cadastrada
    if len(pessoas) == 0:
        pesado = leve = dados[1]

    else:
        if dados[1] > pesado:
            pesado = dados[1]

        if dados[1] < leve:
            leve = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resposta = input("Quer continuar? [S/N] ").upper().strip()

    if resposta == "N":
        break

print("-=" * 30)
print(f"Ao todo você cadastrou {len(pessoas)} pessoas")

print(f"O maior peso foi {pesado:.1f} kg. Peso de:", end=" ")
for pessoa in pessoas:
    if pessoa[1] == pesado:
        print(pessoa[0], end=" ")

print()

print(f"O menor peso foi {leve:.1f} kg. Peso de:", end=" ")
for pessoa in pessoas:
    if pessoa[1] == leve:
        print(pessoa[0], end=" ")
