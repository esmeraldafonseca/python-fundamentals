matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = soma3c = maior2l = 0

for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f"Digite o valor da posição {c, l}: "))

        # Soma dos pares
        if matriz[c][l] % 2 == 0:
            somapar += matriz[c][l]

        # Soma da terceira coluna
        if l == 2:
            soma3c += matriz[c][l]

        # Maior valor da segunda linha
        if c == 1:
            if l == 0:
                maior2l = matriz[c][l]
            elif matriz[c][l] > maior2l:
                maior2l = matriz[c][l]

print("=-"*30)

for c in range (0,3):
    for l in range(0,3):
        print(f"[{matriz[c][l]:^5}]", end="")
    print()

print(f"A soma dos valores pares é: {somapar}")
print(f"A soma dos valores da terceira coluna é: {soma3c}")
print(f"O maior valor da segunda linha é {maior2l}")
