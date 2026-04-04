matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
somaPar = soma3c = maior2l = 0

for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f"Digite o valor da posição {c, l}: "))

print("-="*20)
for c in range(0,3):
    for l in range(0,3):
        print(f"[{matriz[c][l]:^5} ]",end="")
        if matriz[c][l] % 2 ==0:
            somaPar += matriz[c][l]
    print()
print("-="*20)
print(f"A soma dos valores pares é: {somaPar}")

for l in range(0,3):
    soma3c += matriz[l][2]
print(f"Asoma dos valores da terceira coluna são: {soma3c}")

for c in range(0,3):
    if c ==0:
        maior2l= matriz[c][1]
    elif matriz [c][1]> maior2l:
        maior2l = matriz[c][1]
print(f"O maior valor da segunda linha é: {maior2l}")
