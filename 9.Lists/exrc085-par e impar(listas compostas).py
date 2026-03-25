impar = []
par = []
numeros = [impar, par]


for c in range(1, 8):
    num = int(input(f"Digite o {c}º valor: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)


par.sort()
impar.sort()
print("=-=" *30)
print(f"Os numeros pares digitados foram {par}\n Os impares foram {impar}")
