matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input("Digite um numero: "))

print("-="*30)
for c in range(0,3):
    for l in range(0,3):
        print(f"{matriz[c][l]:^5} ",end="")
    print()

