n = s = t = 0

while True :

    n = int(input('DIgite um número[PARAR=999]: '))
    if n == 999:
        break
    s += n
    t += 1
print(f'Digitaste {t} numeros e a soma de todos os numeros digitados é {s}')