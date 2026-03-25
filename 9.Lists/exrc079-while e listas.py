Num = []
resposta = "S"

while resposta=="S":
    N= int(input(f"Digite um numero: "))
    if N not in Num:
        Num.append(N)
        resposta = str(input("Quer continuar[S/N]")).upper() .strip()
    else:
        print(f"Valor duplicado, tente novamente")
    if resposta not in "NS":
        print(f"Resposta invalida!")
        resposta = str(input("Quer continuar[S/N]")).upper() .strip()
Num.sort()
print(f"Os numeros digitados foram: {Num}")




