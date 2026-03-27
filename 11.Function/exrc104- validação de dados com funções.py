def leiaInt(msg):
    ok = False
    valor =0
    while True:
        n = str(input(msg))
        if n.isnumeric():
           valor = int(n)
           ok = True
        else:
            print(f'\033[0;31m ERRO. Digite um numero inteiro valido!\033[m')
        if ok:
            break
    return valor

#programa principal
n = leiaInt("Digite um numero: ")
print(f"Voce digitou o numero {n}")