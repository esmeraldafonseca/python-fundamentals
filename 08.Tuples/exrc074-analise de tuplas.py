
"""
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))

n = (n1, n2, n3, n4)"""

n = (int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')),
     )


print(f'Os numeros digitados foram: {n}')

print(f'O numeros 9 pareceu {n.count(9)} vezes ')
if 3 in n:
    print(f'O primeiro numero 3 apareceu na posição {n.index(3) + 1} º')
else:
    print(f'Não existe numero 3 na lista {n}')

for i in n:
    if i % 2 == 0:
        print(f'Os numeros pares encontrados foram {i}', end=' ')
