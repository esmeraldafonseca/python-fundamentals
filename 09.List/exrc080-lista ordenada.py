lista = list ()

for c in range (0,5):
    item = int (input("Digite um numero: "))
    if c == 0 or item > lista[-1]:
        lista.append(item)
        print(f"Adicionado ao final da lista ")
    else:
        pos = 0
        while pos < len(lista):
            if item <= lista[pos]:
                lista.insert(pos, item)
                print(f"adicionado na posiçãon {pos} da lista ")
                break
            pos += 1

print("="*20)
print("os numeros digitados organizados foram: ", lista)
