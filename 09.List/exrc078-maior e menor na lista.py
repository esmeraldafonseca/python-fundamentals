
num = []
maior = menor = 0

for c in range(0, 5):

    k= int(input(f"Digite um numero na posição {c + 1}: "))
    num.append(k)

   # num.append(int(input("Digite um valor: ")))
    if c == 0:
        maior = menor = k
    else:
        if k > maior:
            maior = k
        if k < menor:
            menor = k

print("=-" *30)
print(f"Você digitou os Valores {num}")
print(f"o maior valor digitado foi {maior} nas posições", end="")
for i, v in enumerate(num):
    if v == maior:
        print(f": {i}...", end=" ")

print(f"\no menor valor digitado foi {menor} nas posições", end="")
for i, v in enumerate(num):
    if v == menor:
        print(f": {i}...", end=" ")
