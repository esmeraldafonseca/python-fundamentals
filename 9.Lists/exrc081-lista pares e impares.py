lista = []
listaPares = []
listaImpares = []
resposta = "S"
while resposta == "S":
    n = int(input("Digite um numero: "))
    lista.append(n)
    resposta =str (input("Deseja continuar? [S/N] ")).upper().strip()
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)

print(f"Lista de numeros digitados: {lista}")
print(f"Lista de numeros pares: {listaPares}")
print(f"Lista de numeros impares: {listaImpares}")
