expressao = str(input("Digite uma expressaõ matematica"))
veri = list()
for simb in expressao:
    if simb == '(':
        veri.append('(')
    elif simb == ')':
        if veri[-1] == ')':
            veri.pop()
        else :
            veri.append(')')
            break

if veri[-1] == 0:
    print("A sua expressao esta correta")
else:
    print("A sua expressao não esta correta")

