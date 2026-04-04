from random import randint
from time import sleep


palpite = []
jogos = []
cont =0
total = 1

print(f"-"*30)
print(f"    EURO MILHÕES")
print("-"*30)

QntPalpites = int(input("Quantos palpites queres gerar?:"))

while total <= QntPalpites:
    cont += 1
    while True :
        sorte = randint(1, 60)
        if sorte not in palpite:
            palpite.append(sorte)
            cont += 1
        elif cont >= 6:
            break
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
    total += 1


print(f"-="*3, f"GERANDO {QntPalpites} PALPITES ", f"-="*3)

for i, l in enumerate(jogos):
    sleep(2)
    print(f"Palpite {i+1}: {l}")


print(f"-="*7, "FIM", "-="*7)




